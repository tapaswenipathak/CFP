from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organizer(models.Model):
    organizer_name = models.OneToOneField(User, on_delete=models.CASCADE)

class Event(models.Model):
    event_name = models.CharField(max_length=100, blank=True)
    event_organizer = models.OneToOneField(Organizer, on_delete=models.CASCADE)
    event_website = models.URLField(blank=True)
    event_start_date = models.DateField(blank=True, null=True)
    event_end_date = models.DateField(blank=True, null=True)
    event_description = models.TextField(blank=True)
    code_of_conduct = models.TextField(blank=True)
