from django.shortcuts import get_object_or_404
from apps.users.models import User
from ..models import Announces, ConservationStatus


def create_announce_service(validated_data, request_user):
    conservation_status = get_object_or_404(
        ConservationStatus, pk=validated_data["conservation_status_id"]
    )

    author_id = validated_data.get("author_id")
    author = get_object_or_404(User, pk=author_id) if author_id else request_user

    announce = Announces.objects.create(
        title=validated_data["title"],
        description=validated_data.get("description", ""),
        type=validated_data["type"],
        conservation_status=conservation_status,
        user=request_user,
        author=author,
    )
    return announce



