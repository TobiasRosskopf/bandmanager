from datetime import timedelta
from datetime import time
from datetime import date
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User    
from tastypie.models import create_api_key


# Signal for generating API-Key when new User is created
models.signals.post_save.connect(create_api_key, sender=User)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user',]

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.last_name}, {self.user.first_name}"
        else:
            return f"{self.user}"

def create_person(sender, **kwargs):
    if kwargs.get('created') is True:
        Person.objects.create(user=kwargs.get('instance'))

models.signals.post_save.connect(create_person, sender=User)



class Band(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    class Meta:
        ordering = ['name',]
    
    def __str__(self):
        return f"{self.name}"


class Membership(models.Model):
    ROLES = [
        ('M', 'Manager'),
        ('B', 'Bandmember'),
        ('S', 'Staff'),
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLES)
    date_joined = models.DateField()

    class Meta:
        ordering = ['person__user__last_name',]

    def __str__(self):
        return f"{self.person} --> {self.band}"


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
