from django.urls import path
from .views import AnnouncesView
from .views_test import TestAnnounceView

urlpatterns = [
    path('announces/', AnnouncesView.as_view(), name='announce-list'),
    path('announces/<int:pk>/update/', AnnouncesView.as_view(), name='announce-update'),
    path('announces/test/', TestAnnounceView.as_view(), name='announce-test'),
]