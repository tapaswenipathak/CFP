from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import User, Speaker, Organizer


class OrganizerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organizer = True
        user.save()
        organizer = Organizer.objects.create(user=user)
        return user

class SpeakerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_speaker = True
        user.save()
        speaker = Speaker.objects.create(user=user)
        return user
