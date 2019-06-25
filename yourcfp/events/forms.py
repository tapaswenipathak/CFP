from django import forms
from django.template.defaultfilters import slugify

from .models import Conference
from proposals.models import  ProposalStatus, Feedback

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'description', 'start_date', 'end_date', 'twitter_id', 'venue']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text']

class ProposalStatusForm(forms.ModelForm):
    class Meta:
        model = ProposalStatus
        fields = ['proposal_status']

CONFERENCE_CHOICES = (
    ('all' , 'Show all submitted proposals'),
    ('pending_reviews' , 'Show all proposals to be reviewed'),
    ('accepted' , 'Show all accepted proposals'),
    ('rejected' , 'Show all rejected proposals'),
)

class ConferenceDashboardForm(forms.Form):
    options = forms.ChoiceField(choices=CONFERENCE_CHOICES, widget=forms.RadioSelect)
