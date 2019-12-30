from datetime import timedelta
from datetime import time
from datetime import date
from datetime import datetime

from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ['name',]
    
        def __str__(self):
            return f"{self.name}"


class Song(models.Model):
    name = models.CharField(max_length=200)
    interpret = models.CharField(max_length=200, default="")
    duration = models.DurationField(default=timedelta(minutes=0))
    active = models.BooleanField(default=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ['name', 'interpret',]

    def __str__(self):
        return f"{self.name} ({self.interpret})"

    def duration_mmss(self):
        dt = datetime(2000, 1, 1, 0, 0) + self.duration
        return dt.strftime("%M:%S")


class Gig(models.Model):
    date = models.DateField(default=date(2000, 1, 1), null=True)
    time = models.TimeField(default=time(0), null=True)
    event = models.CharField(max_length=200, default="", null=True)
    location = models.CharField(max_length=200, default="")
    songs = models.ManyToManyField(Song)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ['-date', '-time',]
    
    def __str__(self):
        date_str = date.strftime(self.date, "%d.%m.%Y")
        return f"{date_str} - {self.location}"

    def time_hhmm(self):
        return self.time.strftime("%H:%M")
