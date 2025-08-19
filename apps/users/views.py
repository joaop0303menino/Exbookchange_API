from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from apps.users.service.UserService import UserService
from apps.users.serializers import UserSerializer

class UserViews(APIView):
    def __init__(self):
        self.user_service = UserService()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"status": "success", "message": "User created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)