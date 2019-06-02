from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from .models import Speaker
from .permissions import set_speaker_permission, set_organizer_permission

User = get_user_model()

@receiver(post_save, sender=User)
def set_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.is_speaker:
            set_speaker_permission(instance)
        if instance.is_organizer:
            set_organizer_permission(instance)
