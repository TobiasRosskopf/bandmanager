from datetime import timedelta

from django.db import models
from django.utils.dateparse import parse_duration


class Song(models.Model):
    name = models.CharField(max_length=200)
    interpret = models.CharField(max_length=200)
    duration = models.DurationField(default=timedelta(minutes=0))
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.interpret})"

    def duration_mmss(self):
        # duration = parse_duration(self.duration)

        # seconds = duration.seconds

        # minutes = seconds // 60
        # seconds = seconds % 60

        # minutes = minutes % 60

        # return '{:02d}:{:02d}'.format(minutes, seconds)
        return self.duration
