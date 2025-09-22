from django.urls import path
from apps.users import views

urlpatterns = [
  path("exchange-donation-historic/", views.UserViews.as_view(), name="exchange-donation-historic"),
]
