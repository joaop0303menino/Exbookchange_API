from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.books.serializers import AnnounceSerializer
from apps.books.models import Announces, ImagesBook
from .service.CreateAnnounceService import create_announce_service
from .service.UpdateAnnounceService import update_announce

class AnnounceCreateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = AnnounceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        announce = serializer.save(user=request.user)

        images = request.FILES.getlist('images')
        for i, img in enumerate(images):
            ImagesBook.objects.create(
                announce=announce,
                image=img,
                is_cover=(i == 0)
            )
        output_serializer = AnnounceSerializer(announce)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
class AnnounceUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, pk):

        try:
            announce = Announces.objects.get(pk=pk)
        except Announces.DoesNotExist:
            return Response({"detail": "Anúncio não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if announce.user != request.user:
            return Response({"detail": "Você não tem permissão para atualizar este anúncio."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = AnnounceSerializer(instance=announce, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        images = request.FILES.getlist('images')
        if images:
            ImagesBook.objects.filter(announce=announce).delete()
            for i, img in enumerate(images):
                ImagesBook.objects.create(
                    announce=announce,
                    image=img,
                    is_cover=(i == 0)
                )
        return Response(AnnounceSerializer(announce).data, status=status.HTTP_200_OK)