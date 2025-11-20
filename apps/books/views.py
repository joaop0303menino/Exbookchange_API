from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from apps.books.models import Announces, ImagesBook
from apps.books.serializers import AnnounceSerializer

class AnnounceView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        announce_id = request.query_params.get("announce_id")

        if announce_id:
            announce = Announces.objects.filter(id=announce_id).first()

            if announce is None:
                return JsonResponse(
                    {"status": "error", "message": "Announce not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = AnnounceSerializer(announce)
            return JsonResponse(
                {"status": "success", "announce": serializer.data},
                status=200
            )

        announces = Announces.objects.all()

        if not announces.exists():
            return JsonResponse(
                {"status": "error", "message": "No announces found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AnnounceSerializer(announces, many=True)
        return JsonResponse(
            {"status": "success", "announces": serializer.data},
            status=200
        )

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


    def put(self, request, pk):

        try:
            announce = Announces.objects.get(pk=pk)
        except Announces.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "No announces found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if announce.user != request.user:
            return JsonResponse(
                {"status": "error", "message": "You do not have permission to update this announce"}, 
                status=status.HTTP_403_FORBIDDEN
            )

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

    def delete(self, request):
        announce_id = request.data.get("announce_id")

        if not announce_id:
            return JsonResponse(
                {"status": "error", "message": "announce_id is required"},
                status=400
            )

        announce = Announces.objects.filter(id=announce_id, user=request.user).first()

        if announce is None:
            return JsonResponse(
                {"status": "error", "message": "Announce not found or not yours"},
                status=404
            )

        announce.delete()

        return JsonResponse(
            {"status": "success", "message": "Announce deleted"},
            status=200
        )
