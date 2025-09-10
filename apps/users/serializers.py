from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'date_birth', 'email', 'password', 'phone', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}  
        }