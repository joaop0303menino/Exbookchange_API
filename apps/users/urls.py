from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViews.as_view()),
    path('profile/', views.ProfileView.as_view()),
]
