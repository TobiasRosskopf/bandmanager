from django.db import models

from datetime import timedelta

class Song(models.Model):
    name = models.CharField(max_length=200)
    interpret = models.CharField(max_length=200)
    # duration = models.DurationField(default=timedelta(0))

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.interpret})"
