from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
