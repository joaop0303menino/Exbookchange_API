from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExchangeDonationHistoricViews.as_view()),
]
