from django import forms
from django.db.models import Q

from .models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['title', 'outline', 'pitch', 'talktime']

class BulkSubmit(forms.Form):

    proposal_list = forms.MultipleChoiceField()

    def __init__(self, user, *args, **kwargs):
        super(BulkSubmit, self).__init__(*args, **kwargs)
        self.fields['proposal_list'] = forms.MultipleChoiceField(choices=[(proposal.slug, proposal.title) for proposal in Proposal.objects.all().filter(Q(author=user.speaker) & Q(status='draft'))], widget=forms.widgets.CheckboxSelectMultiple())
#
# def __init__(self, user, *args, **kwargs):
#         super(MyForm, self).__init__(*args, **kwargs)
#         self.fields['favorite_color'] = forms.MultipleChoiceField(choices=[(proposal.slug, proposal.title) for proposal in Proposal.objects.all().filter(status='draft')])
    #forms.RadioSelect(choices=list(Proposal.objects.all()))

# class ExampleForm(forms.Form):
#     name = forms.MultipleChoiceField(
#         choices=CHOICES,
#         widget=ColumnCheckboxSelectMultiple(columns=3, css_class='col-md-4', wrapper_css_class='row',)




# class waypointForm(forms.Form):
#     def __init__(self, user, *args, **kwargs):
#         super(waypointForm, self).__init__(*args, **kwargs)
#         self.fields['waypoints'] = forms.ChoiceField(
#             choices=[(o.id, str(o)) for o in Waypoint.objects.filter(user=user)]
