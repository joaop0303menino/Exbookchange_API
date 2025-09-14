from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.UserViews.as_view(), name='user-create'),
]
