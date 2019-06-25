from django import forms
from django.template.defaultfilters import slugify

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['blog_url', 'twitter_handle', 'location', 'bio', 'organization']

CHOICES = (
    ('accepted' , 'Show all accepted proposals'),
    ('rejected' , 'Show all rejected proposals'),
    ('draft' , 'Show all draft proposals'),
    ('published' , 'Show all published proposals')
)

class DashboardForm(forms.Form):
    options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
