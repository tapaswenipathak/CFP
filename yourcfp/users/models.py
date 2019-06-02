
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class User(AbstractUser):
    is_speaker = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

class Speaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
