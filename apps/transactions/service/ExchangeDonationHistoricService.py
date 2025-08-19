from django.http import JsonResponse
from rest_framework import status
from apps.transactions.models import ExchangeDonationHistoric

class ExchangeDonationService:
    def __init__(self):
        self.ExchangeDonation_model = ExchangeDonationHistoric

    def createExchangeDonation(self, **data):
        ExchangeDonationExists = self.getExchangeDonationByEmail(data.email)

        if ExchangeDonationExists:
            return JsonResponse({"status": "error", "message": "ExchangeDonation already exists"}, status=status.HTTP_409_CONFLICT)

        return self.ExchangeDonation_model.objects.create(**data)

    def getExchangeDonationByEmail(self, email):
        return self.ExchangeDonation_model.objects.filter(email=email).first()