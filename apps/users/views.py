from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from apps.users.services.UserService import UserService
from apps.users.serializers import UserSerializer
from apps.users.services.ProfileService import ProfileService

class UserViews(APIView):
    def __init__(self):
        self.user_service = UserService()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"status": "success", "message": "User created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)

class ProfileViews(APIView):
    def __init__(self):
        self.profile_service = ProfileService()

    def post(self, request):
        id_user = request.data.get("id_user")

        if not id_user:
            return JsonResponse({"status": "error", "message": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        response = self.profile_service.createProfile(**request.data)
        return response