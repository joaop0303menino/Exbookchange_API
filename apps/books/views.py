from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.books.serializers import AnnounceSerializer
from apps.books.models import ImagesBook
from .service.CreateAnnounceService import create_announce_service 

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

    