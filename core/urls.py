from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('authentication/', include([
            path('Login/', TokenObtainPairView.as_view()),
            path('Refresh/', TokenRefreshView.as_view()),
        ])),
        path('users/', include('apps.users.urls')),
        path('books/', include('apps.books.urls')),
        path('transactions/', include('apps.transactions.urls')),
        path('notifications/', include('apps.notifications.urls')),
        path('complaints/', include('apps.complaints.urls')),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
