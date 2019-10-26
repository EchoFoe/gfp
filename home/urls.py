from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^photo_and_video/$', views.photo_and_video, name='photo_and_video'),
    url(r'^thanks/$', views.thanks, name='thanks')
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
