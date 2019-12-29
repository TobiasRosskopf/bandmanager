from django.urls import path, include
from tastypie.api import Api

from . import views
from .api import GigResource, SongResource

v1_api = Api(api_name='v1')
v1_api.register(GigResource())
v1_api.register(SongResource())

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.songs, name='songs'),
    path('gigs/', views.gigs, name='gigs'),
    path('api/', include(v1_api.urls)),
]
