from django.middleware.csrf import get_token
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from apps.users.service.UserService import UserService
from apps.users.serializers import UserSerializer

class UserViews(APIView):
    def __init__(self):
        self.user_service = UserService()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = self.user_service.createUser(**serializer.validated_data)
        
        if isinstance(user, JsonResponse):
            return user

        return JsonResponse({"status": "success", "message": "User created successfully","data": {"id": user.id, "full_name": user.full_name, "email": user.email}}, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    user_service = UserService()

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = self.user_service.login_user(email, password)
        
        if user:
            return JsonResponse({"message": "Login realizado com sucesso!"}, status=status.HTTP_200_OK)
        return JsonResponse({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
    
class TokenCSRFView(APIView):
    def get(self, request):
        token = get_token(request)

        return JsonResponse({"status": "success", "message": "CSRF token retrieved successfully", "data": token}, status=status.HTTP_200_OK)