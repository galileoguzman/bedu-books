from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from books.views import home_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_books, name='index'),
]

# Add static and media urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
