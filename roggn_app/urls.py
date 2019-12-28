from django.urls import path, include

from . import views
from .api import GigResource


gig_resource = GigResource()

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'^songs/', views.songs, name='songs'),
    path(r'^api/', include(gig_resource.urls)),
]
