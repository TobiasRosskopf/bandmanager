from django.contrib import admin

# Import models
from .models import Band
from .models import Song
from .models import Gig


# Register models for admin
admin.site.register(Band)
admin.site.register(Song)
admin.site.register(Gig)
