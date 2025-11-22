from django.http import JsonResponse 
from rest_framework import status  
from apps.users.models import User, Profile
from apps.books.models import Announces

class UserService: 
    def __init__(self): 
        self.user_model = User 
        self.profile_model = Profile
        self.announces_model = Announces
             
    def getUser(self, validated_data):
        User = self.user_model.objects.get(id=validated_data.get("id"), is_active=True).first()
        
        if User is None:
            return JsonResponse({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return User
    
    def getUserByEmail(self, email):
        return self.user_model.objects.filter(email=email, is_active=True).first()
        
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
        self.profile_model.objects.create(user=user, nickname=validated_data.get("full_name"))
                
        return user
    
    def deleteUser(self, user_id):
        user = self.user_model.objects.filter(id=user_id, is_active=True).first()
        
        if user is None:
            return JsonResponse({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user.is_active = False
        user.save()
        
        announces = self.announces_model.objects.filter(user_id=user_id)
        for announce in announces:
            announce.is_archived = True
            announce.save()
        
        return JsonResponse({"status": "success", "message": "User deleted successfully"}, status=status.HTTP_200_OK)