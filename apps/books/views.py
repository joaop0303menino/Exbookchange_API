from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, permissions


from apps.books.serializers import AnnounceSerializer
from apps.books.models import ImagesBook
from .service.CreateAnnounceService import create_announce_service 
from .service.UpdateAnnounceService import update_announce

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_announce(request):
    serializer = AnnounceSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    announce = create_announce_service(serializer.validated_data, request.user)

    if serializer.is_valid():         
        images = request.FILES.getlist('images')
        for i, img in enumerate(images):
            ImagesBook.objects.create(
                announce=announce,
                image=img,
                is_cover=(i == 0) 
            )
        output_serializer = AnnounceSerializer(announce)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class AnnounceUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        serializer = AnnounceSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            announce, error = update_announce(pk, request.user, serializer.validated_data)
            if error:
                return Response({"detail": error}, status=status.HTTP_404_NOT_FOUND)
            return Response(AnnounceSerializer(announce).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      