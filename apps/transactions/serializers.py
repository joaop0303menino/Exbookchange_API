from rest_framework import serializers
from .models import ExchangeDonationHistoric

class ExchangeDonationHistoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeDonationHistoric
        fields = "__all__"