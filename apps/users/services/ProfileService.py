from django.http import JsonResponse
from rest_framework import status
from apps.users.models import Profile
from apps.users.services.UserService import UserService
from utils.image_utils import ImageUtils

class ProfileService:
    def __init__(self):
        self.profile_model = Profile
        self.userService = UserService()
        self.image_utils = ImageUtils()

    def createProfile(self, **data):
        profileExists = self.getProfileByIdUser(data["id_user"])

        if profileExists:
            return JsonResponse({"status": "error", "message": "Profile already exists"}, status=status.HTTP_409_CONFLICT)

        user = self.userService.getUserById(data["id_user"])

        if not user:
            return JsonResponse({"status": "error", "message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        image_bytes = data.get("photo")

        image_png = self.image_utils.convert_bytes_to_image(image_bytes)

        image_path = self.image_utils.save_image_in_server(image_png, f"profile_photo_user_{user.id}.png")

        profile = self.profile_model(**data)
        profile.user = user
        profile.photo = image_path
        profile.save()

        return JsonResponse({"status": "success", "message": "Profile created successfully", "data": profile}, status=status.HTTP_201_CREATED)

    def getProfileByIdUser(self, id_user):
        return self.profile_model.objects.select_related("user").get(user_id=id_user)
