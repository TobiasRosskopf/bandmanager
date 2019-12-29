from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication

from .models import Gig, Song


class GigResource(ModelResource):
    
    class Meta:
        queryset = Gig.objects.all()
        resource_name = 'gigs'
        authentication = ApiKeyAuthentication()
        # http://127.0.0.1:8000/api/v1/gigs/?username=tobias.rosskopf&api_key=sdsdfsdfsdfsdfsdfs


class SongResource(ModelResource):
    
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'songs'
        authentication = ApiKeyAuthentication()
        # http://127.0.0.1:8000/api/v1/songs/?username=tobias.rosskopf&api_key=sdsdfsdfsdfsdfsdfs
