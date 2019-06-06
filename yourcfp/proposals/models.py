from django.db import models
from django.contrib.auth import get_user_model
from events.models import Conference
from users.models import Speaker
User = get_user_model()

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Proposal(models.Model):
    author = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    name = models.ForeignKey(Conference, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,  default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f'{self.author}\'s {self.name} proposal'
