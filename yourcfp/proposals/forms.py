from django import forms
from .models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['title', 'outline', 'pitch', 'talktime']

class BulkSubmit(forms.Form):

    x = Proposal.objects.all()
    x = x.filter(status='draft')
    print('*************************************')
    print(x)
    print('*************************************')
    d=[]
    for i in x:
        d.append((i.slug, i.title))
    proposal_list = forms.MultipleChoiceField(choices=d,
    widget=forms.widgets.CheckboxSelectMultiple())

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
