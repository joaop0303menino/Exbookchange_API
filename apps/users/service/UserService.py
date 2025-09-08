from django.http import JsonResponse 
from rest_framework import status 
from apps.users.models import User 

class UserService: 
    def __init__(self): 
        self.user_model = User 
        
    def createUser(self, validated_data): 
        email = validated_data.get("email") 
        userExists = self.getUserByEmail(email) 
         
        if userExists: 
            return JsonResponse({"status": "error", "message": "User already exists"}, status=status.HTTP_409_CONFLICT) 
        
        user = self.user_model( 
            full_name=validated_data.get("full_name"), 
            date_birth=validated_data.get("date_birth"),
            email=email, 
            phone=validated_data.get("phone"), ) 
        
        user.set_password(validated_data['password']) 
        user.save() 
        
        return user

    def getUserByEmail(self, email):
        return self.user_model.objects.filter(email=email).first()

    def getUserById(self, id):
        return self.user_model.objects.filter(id=id).first()
    
    def login(self, email, password):
        user = self.getUserByEmail(email)

        if not user or not user.check_password(password):
            return JsonResponse({"status": "error", "message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return user