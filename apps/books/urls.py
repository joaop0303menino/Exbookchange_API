from django.urls import path
from .views import create_announce, AnnounceUpdateView

urlpatterns = [
    path('announces/create/', create_announce, name='announce-create'),
    path('announces/<int:pk>/update/', AnnounceUpdateView.as_view(), name='announce-update'),
]