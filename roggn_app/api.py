from tastypie.resources import ModelResource, ALL
from tastypie.authentication import ApiKeyAuthentication
from tastypie.serializers import Serializer

from .models import Gig, Song


class GigResource(ModelResource):
    
    class Meta:
        queryset = Gig.objects.all()
        resource_name = 'gigs'
        fields = ['date', 'time', 'event', 'location']
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        serializer = Serializer(formats=['json', 'xml'])
        # http://127.0.0.1:8000/api/v1/gigs/?username=tobias.rosskopf&api_key=sdsdfsdfsdfsdfsdfs


class SongResource(ModelResource):
    
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'songs'
        fields = ['name', 'interpret', 'duration', 'active']
        allowed_methods = ['get']
        filtering = {
            'interpret': ALL,
        }
        authentication = ApiKeyAuthentication()
        serializer = Serializer(formats=['json', 'xml'])
        # http://127.0.0.1:8000/api/v1/songs/?username=tobias.rosskopf&api_key=sdsdfsdfsdfsdfsdfs
