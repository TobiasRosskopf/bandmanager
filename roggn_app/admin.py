from django.contrib import admin

# Import models
from .models.models import Person
from .models.models import Band
from .models.models import Membership
from .models.models import Song
from .models.models import Gig


# Register models for admin
admin.site.register(Person)
admin.site.register(Band)
admin.site.register(Membership)
admin.site.register(Song)
admin.site.register(Gig)
