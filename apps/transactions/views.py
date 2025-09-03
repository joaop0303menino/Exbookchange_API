from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.transactions.serializers import ExchangeDonationHistoricSerializer
from apps.transactions.service.ExchangeDonationHistoricService import ExchangeDonationService
from apps.users.models import Profile
from apps.books.models import Announces

class ExchangeDonationHistoricViews(APIView):
    def __init__(self):
        self.service = ExchangeDonationService()

    def post(self, request):
        data = request.data

        user_receiver_name = data.get("user_receiver")
        user_receiver = Profile.objects.filter(nickname=user_receiver_name).first()

        if not user_receiver:
            return Response({
                "status": "error",
                "message": f"Usuário '{user_receiver_name}' não encontrado."
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ExchangeDonationHistoricSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        announce_id = data.get("id_announce")
        announce = get_object_or_404(Announces, id=announce_id)
        announce.is_archived = True
        announce.save()


        return Response({
            "status": "success",
            "message": "Transação registrada com sucesso",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
