from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from utils.csrf import TokenCSRFView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('authentication/', include([
            path('csrf-token/', TokenCSRFView.as_view(), name='csrf-token'),
            path('login/', TokenObtainPairView.as_view()),
            path('refresh/', TokenRefreshView.as_view()),
        ])),
        path('', include('apps.users.urls')),
        path('', include('apps.books.urls')),
        path('', include('apps.transactions.urls')),
        path('', include('apps.notifications.urls')),
        path('', include('apps.complaints.urls')),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
