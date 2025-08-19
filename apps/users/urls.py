from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserViews.as_view()),
]
