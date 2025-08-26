from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=150)  
    date_birth = models.DateField(null=True, blank=True)  
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=128)  
    phone = models.CharField(max_length=20, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.full_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nickname = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nickname