from datetime import timedelta

from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=200)
    interpret = models.CharField(max_length=200)
    duration = models.DurationField(default=timedelta(minutes=0))
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.interpret})"

    def duration_mmss(self):
        # TODO: Convert to mm:ss
        return self.duration


class Setlist(models.Model):
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return len(self.songs)


class Gig(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=200)
    setlist = models.ForeignKey(Setlist)

    def __str__(self):
        return f"{self.date} - {self.location}"
