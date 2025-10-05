from django.urls import path
from apps.transactions.views import ExchangeDonationHistoricViews

urlpatterns = [
  path("exchange-donation-historic", ExchangeDonationHistoricViews.as_view(), name="exchange-donation-historic"),
]
