
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_speaker = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)

class Speaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
