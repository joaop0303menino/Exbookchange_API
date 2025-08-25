from django.shortcuts import get_object_or_404
from apps.books.models import Author
from apps.users.models import User
from ..models import Announces, ConservationStatus


def create_announce_service(validated_data, request_user):
    conservation_status = get_object_or_404(
        ConservationStatus, pk=validated_data["conservation_status_id"]
    )

    author_full_name = validated_data.pop("author_full_name")
    author, _ = Author.objects.get_or_create(full_name=author_full_name)

    announce = Announces.objects.create(
        title=validated_data["title"],
        description=validated_data.get("description", ""),
        type=validated_data["type"],
        conservation_status=conservation_status,
        user=request_user,
        author=author,
    )
    return announce



