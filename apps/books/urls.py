from django.urls import path
from .views import AnnounceCreateView, AnnounceUpdateView

urlpatterns = [
    path('announces/create/', AnnounceCreateView.as_view(), name='announce-create'),
    path('announces/<int:pk>/update/', AnnounceUpdateView.as_view(), name='announce-update'),
]