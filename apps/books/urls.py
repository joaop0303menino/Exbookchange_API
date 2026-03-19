from django.urls import path
from .views import AnnounceView

urlpatterns = [
    path('announces/', AnnounceView.as_view(), name='announce-test'),
    path('announces/<int:pk>/update', AnnounceView.as_view(), name='announce-test'),
]