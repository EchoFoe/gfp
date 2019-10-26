from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^', include('broadcast.urls')),
    url(r'^', include('documents.urls')),
    url(r'^', include('doping_testing.urls')),
    url(r'^', include('sportsman.urls')),
    url(r'^', include('tournaments.urls')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
