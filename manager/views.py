from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Song


def songs(request):
    songs_active = Song.objects.filter(active=True)
    songs_not_active = Song.objects.filter(active=False)

    template = loader.get_template('manager/songs.html')
    context = {
        'songs_active': songs_active,
        'songs_not_active': songs_not_active,
    }
    
    return HttpResponse(template.render(context, request))
