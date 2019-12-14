from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Song


def songs(request):
    song_list = Song.objects.order_by('name')
    template = loader.get_template('manager/songs.html')
    context = {
        'song_list': song_list,
    }
    return HttpResponse(template.render(context, request))
