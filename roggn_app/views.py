from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Import models
from .models.models import Song
from .models.models import Gig


def index(request):
    template = loader.get_template('roggn_app/index.html')
    context = {}
    
    return HttpResponse(template.render(context, request))


def songs(request):
    songs_active = Song.objects.filter(active=True)
    songs_passiv = Song.objects.filter(active=False)

    template = loader.get_template('roggn_app/songs.html')
    context = {
        'songs_active': songs_active,
        'songs_passiv': songs_passiv,
    }
    
    return HttpResponse(template.render(context, request))


def gigs(request):
    # TODO: Get objects!
    template = loader.get_template('roggn_app/gigs.html')
    context = {
        #TODO: Place content!
    }
    
    return HttpResponse(template.render(context, request))
