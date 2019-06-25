from django import forms
from django.template.defaultfilters import slugify

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['blog_url', 'twitter_handle', 'location', 'bio', 'organization']

SPEAKER_CHOICES = (
    ('accepted' , 'Show all accepted proposals'),
    ('rejected' , 'Show all rejected proposals'),
    ('draft' , 'Show all draft proposals'),
    ('published' , 'Show all published proposals')
)

class SpeakerDashboardForm(forms.Form):
    options = forms.ChoiceField(choices=SPEAKER_CHOICES, widget=forms.RadioSelect)
