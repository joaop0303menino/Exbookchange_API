from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

class TokenCSRFView(APIView):
    def get(self, request):
        token = get_token(request)

        return JsonResponse({"status": "success", "message": "CSRF token retrieved successfully", "data": token}, status=status.HTTP_200_OK)