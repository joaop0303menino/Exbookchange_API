from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('books/', include('apps.books.urls')),
    path('transactions/', include('apps.transactions.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('complaints/', include('apps.complaints.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
