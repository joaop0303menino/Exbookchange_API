from django.urls import path
from . import views

urlpatterns = [
    path('', views.TokenCSRFView.as_view()),
]