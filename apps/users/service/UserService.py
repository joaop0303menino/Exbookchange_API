from django.http import JsonResponse
from rest_framework import status
from apps.users.models import User, Profile


class UserService:
    def __init__(self):
        self.user_model = User
        self.profile_model = Profile    

    def createUser(self, **data):
        userExists = self.getUserByEmail(data["email"])

        if userExists:
            return JsonResponse({"status": "error", "message": "User already exists"}, status=status.HTTP_409_CONFLICT)

        user =  self.user_model.objects.create(**data)
        self.profile_model.objects.create(user=user, nickname=data.get("full_name"))
        
        return user

    def getUserByEmail(self, email):
        return self.user_model.objects.filter(email=email).first()

    def getUserById(self, id):
        return self.user_model.objects.filter(id=id).first()