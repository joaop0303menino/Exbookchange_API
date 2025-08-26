from django.http import JsonResponse
from rest_framework import status
from apps.users.models import User


class UserService:
    def __init__(self):
        self.user_model = User

    def createUser(self, **data):
        userExists = self.getUserByEmail(data.email)

        if userExists:
            return JsonResponse({"status": "error", "message": "User already exists"}, status=status.HTTP_409_CONFLICT)

        return self.user_model.objects.create(**data)

    def getUserByEmail(self, email):
        return self.user_model.objects.filter(email=email).first()

    def getUserById(self, id):
        return self.user_model.objects.filter(id=id).first()