from django.urls import path
from .views import create_announce  # importa as views do app

urlpatterns = [
   path("announces/", create_announce, name="create_announce"),
]
