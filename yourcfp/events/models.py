from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Conference(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.TextField(default="")
    twitter_id = models.CharField(max_length=100, blank=True, null=True, default='')

    def __str__(self):
        return self.name
