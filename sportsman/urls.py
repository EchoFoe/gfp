from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^sportsman/$', views.sportsman, name='sportsman'),
]