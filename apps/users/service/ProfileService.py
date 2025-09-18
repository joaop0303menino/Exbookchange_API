from django.http import JsonResponse
from rest_framework import status
from apps.users.models import Profile

class ProfileService:
    def __init__(self):
        self.profile_model = Profile

    def updateProfile(self, validated_data):
        user_id = validated_data.get("user_id")
        profile = self.profile_model.objects.get(user_id=user_id)
        
        if profile is None:
            return JsonResponse({"status": "error", "message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        nickname = validated_data.get("nickname")
        description = validated_data.get("description")
        photo = validated_data.get("photo")

        if nickname:
            profile.nickname = nickname
        if description:
            profile.description = description
        if photo:
            profile.photo = photo

        profile.save()
        return profile