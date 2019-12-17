from django.contrib import admin

from .models import Song, Setlist, Gig

admin.site.register(Song)
admin.site.register(Setlist)
admin.site.register(Gig)
