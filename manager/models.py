from datetime import timedelta
from datetime import time
from datetime import date

from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=200)
    interpret = models.CharField(max_length=200)
    duration = models.DurationField(default=timedelta(minutes=0))
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.interpret})"

    def duration_mmss(self):
        # TODO: Convert to mm:ss
        return self.duration


class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField(default=time(0))
    location = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)
    
    class Meta:
        ordering = ['date', 'time']
    
    def __str__(self):
        date_str = date.strftime(self.date, "%d.%m.%Y")
        return f"{date_str} - {self.location}"
