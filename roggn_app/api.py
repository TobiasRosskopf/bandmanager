from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer

from .models.models import Song
from .models.models import Gig


class GigResource(ModelResource):
    
    class Meta:
        queryset = Gig.objects.all()
        resource_name = 'gigs'
        fields = ['date', 'time', 'event', 'location']
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        serializer = Serializer(formats=['json', 'xml'])
        # http://127.0.0.1:8000/api/v1/gigs/?username=tobias.rosskopf&api_key=sdsdfsdfsdfsdfsdfs&format=json


class SongResource(ModelResource):
    
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'songs'
        fields = ['name', 'interpret', 'duration', 'active']
        allowed_methods = ['get']
        filtering = {
            'active': ALL,
        }
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'xml'])

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)
        
        # http://127.0.0.1:8000/api/v1/songs/?username=tobias.rosskopf&api_key=sdsdfsdfsdfsdfsdfs&format=json&active=True
        # http://127.0.0.1:8000/api/v1/songs/?username=test_user_01&api_key=84f93bf313ef5112218a45e74ba0c14079541e38
