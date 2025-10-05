from django.urls import path
from .views import AnnouncesView

urlpatterns = [
    path('announces/', AnnouncesView.as_view(), name='announce-list'),
    path('announces/<int:pk>/update/', AnnouncesView.as_view(), name='announce-update'),
]