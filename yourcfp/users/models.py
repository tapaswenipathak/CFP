from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

talk_formats = [
    (1, 'Talk(30-45 mins)'),
    (2, 'Lightning Talks(5-10 mins)'),
    (3, 'Workshop(more than 60 mins)'),
    (4, 'Other')
]

auidence_type = [
    (1, 'Beginner'),
    (2, 'Intermediate'),
    (3, 'Advanced')
]

class Proposal(models.Model):
    speaker = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    elevator_pitch = models.CharField(max_length=300)
    talk_format = models.IntegerField(choices=talk_formats)
    auidence_level = models.IntegerField(choices=auidence_type)
    description = models.TextField()
    notes = models.TextField()
