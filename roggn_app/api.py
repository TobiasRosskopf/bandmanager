"""
https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3
"""

from tastypie.resources import ModelResource

from .models import Gig


class GigResource(ModelResource):
    class Meta:
        queryset = gig.objects.all()
        resource_name = 'gig'
