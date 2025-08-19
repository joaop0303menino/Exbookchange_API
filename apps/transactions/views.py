from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from apps.transactions.service.ExchangeDonationHistoricService import ExchangeDonationService
from apps.transactions.serializers import ExchangeDonationHistoricSerializer

class ExchangeDonationHistoricViews(APIView):
    def __init__(self):
        self.user_service = ExchangeDonationService()

    def post(self, request):
        serializer = ExchangeDonationHistoricSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"status": "success", "message": "transactions created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)