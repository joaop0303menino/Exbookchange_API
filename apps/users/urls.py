from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViews.as_view(), name='user-create'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('csrf-token/', views.TokenCSRFView.as_view(), name='csrf-token'),
]
