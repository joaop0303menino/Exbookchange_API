import rest_framework.decorators
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.transactions.serializers import ExchangeDonationHistoricSerializer
from apps.transactions.service.ExchangeDonationHistoricService import ExchangeDonationService
from apps.books.models import Announces
from apps.users.service.UserService import UserService
from apps.users.models import User

class ExchangeDonationHistoricViews(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.service = ExchangeDonationService()
        self.user_service = UserService()

    def post(self, request):

        data = request.data
        
        announce_id = int(data.get("id_announce"))
        user_receiver_id = int(data.get("user_receiver"))
        user_contributor_id = int(data.get("id_user"))

        if not all([announce_id, user_receiver_id, user_contributor_id]):
            return Response({
                "status": "error",
                "message": "Fields are required: id_announce, user_receiver, id_user"
            }, status=status.HTTP_400_BAD_REQUEST)

        if user_receiver_id == user_contributor_id:
            return Response({
                "status": "error",
                "message": "You cannot exchange or donate to yourself."
            }, status=status.HTTP_400_BAD_REQUEST)

        announce = get_object_or_404(Announces, id=announce_id)
        user_receiver = get_object_or_404(User, id=user_receiver_id)
        user_contributor = get_object_or_404(User, id=user_contributor_id)

        transaction = self.service.create_exchange(
            id_user=user_contributor,
            id_announce=announce,
            user_receiver=user_receiver
        )
        
        announce.is_archived = True
        announce.save()

        serializer = ExchangeDonationHistoricSerializer(transaction)

        return Response({
            "status": "success",
            "message": "Transaction recorded successfully.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
