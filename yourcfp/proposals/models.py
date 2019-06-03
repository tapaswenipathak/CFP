from django.db import models
from django.contrib.auth import get_user_model
from events.models import Conference
from users.models import Speaker
User = get_user_model()

# Create your models here.
class Proposal(models.Model):
    author = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    name = models.ForeignKey(Conference, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.author.username}\'s {self.name} proposal'
