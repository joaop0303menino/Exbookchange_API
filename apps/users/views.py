from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from apps.users.models import User
from apps.users.service.UserService import UserService
from apps.users.service.ProfileService import ProfileService
from apps.users.serializers import UserSerializer

class UserViews(APIView):
    def __init__(self):
        self.user_service = UserService()
        
    def get(self, request):
        user_id = request.query_params.get("user_id")
        
        if not user_id:
            return JsonResponse(
                {"status": "error", "message": "User ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = self.user_service.getUserById(user_id)

        if user is None or not user.is_active:
            return JsonResponse(
                {"status": "error", "message": "User not found or inactive"},
                status=status.HTTP_404_NOT_FOUND
            )

        return JsonResponse({
            "status": "success",
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "date_birth": user.date_birth,
                "phone": user.phone,
                "is_active": user.is_active
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = self.user_service.createUser(serializer.validated_data)
        
        if isinstance(user, JsonResponse):
            return user

        return JsonResponse({"status": "success", "message": "User created successfully","data": {"id": user.id, "full_name": user.full_name, "email": user.email}}, status=status.HTTP_201_CREATED)
    
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
   
    def __init__(self):
        self.profile_service = ProfileService()
        
    def get(self, request):
        user_id = request.query_params.get("user_id")
        profile = self.profile_service.getProfile({"user_id": user_id})
        
        if profile is None:
            return JsonResponse({"status": "error", "message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({
            "status": "success",
            "profile": {
                "nickname": profile.nickname,
                "description": profile.description,
                "photo": profile.photo.url if profile.photo else None
            }
        }, status=status.HTTP_200_OK)
        

    def put(self, request):

        profile = self.profile_service.updateProfile(request.data)
        
        if profile is None:
            return JsonResponse({"status": "error", "message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({
            "status": "success",
            "message": "User and profile updated successfully",
            "profile": {
                    "nickname": profile.nickname,
                    "description": profile.description,
                    "photo": profile.photo.url if profile.photo else None
                }
            
        }, status=status.HTTP_200_OK)
    