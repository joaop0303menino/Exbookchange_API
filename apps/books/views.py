from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.books.serializers import AnnounceSerializer
from .service.CreateAnnounceService import create_announce_service 


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_announce(request):
    serializer = AnnounceSerializer(data=request.data)
    if serializer.is_valid():
        announce = create_announce_service(serializer.validated_data, request.user)
        output_serializer = AnnounceSerializer(announce)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)