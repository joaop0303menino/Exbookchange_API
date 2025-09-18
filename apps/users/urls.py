from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViews.as_view(), name='user-create'),
    path('profile/<int:user_id>/', views.UpdateProfileView.as_view(), name='update-profile'),
]
