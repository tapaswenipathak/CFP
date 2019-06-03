from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from users.models import Organizer

User = get_user_model()

# Create your models here.
class Conference(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(default="")
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.TextField(default="")
    twitter_id = models.CharField(max_length=100, blank=True, null=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Conference, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
