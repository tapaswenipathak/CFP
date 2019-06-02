from django import forms
from django.template.defaultfilters import slugify

from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'description', 'start_date', 'end_date', 'twitter_id', 'venue']
        
