from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Conference
from .forms import ConferenceForm, FeedbackForm, ProposalStatusForm
from proposals.models import Proposal

User = get_user_model()

# Create your views here
class UserConferenceList(UserPassesTestMixin, ListView):
    model = Conference

    def get_queryset(self):
        return Conference.objects.filter(organizer=self.request.user.organizer)

    def test_func(self):
        user = self.request.user
        if user.is_organizer:
            return True
        return False

class ConferenceProposalListView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Proposal
    permission_required = 'proposals.view_proposal'

    def get_queryset(self):
        conference = Conference.objects.get(slug=self.kwargs['slug'])
        return conference.proposal_set.filter(status='published')

    def test_func(self):
        user = self.request.user
        if user.is_organizer:
            return True
        return False

class ConferenceList(ListView):
    model = Conference

class ConferenceDetailView(DetailView):
    model = Conference
    query_pk_and_slug = True

class ConferenceCreateView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Conference
    fields = ['name', 'description', 'start_date', 'end_date', 'venue', 'twitter_id']
    success_url=reverse_lazy('events:conference-list')
    permission_required = 'events.add_conference'

    def form_valid(self, form):
        form.instance.organizer = self.request.user.organizer
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.is_organizer:
            return True
        return False

class ConferenceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Conference
    fields = ['name', 'description', 'start_date', 'end_date', 'venue', 'twitter_id']
    success_url=reverse_lazy('events:conference-list')
    permission_required = 'events.change_conference'

    def form_valid(self, form):
        form.instance.organizer = self.request.user.organizer
        return super().form_valid(form)

    def test_func(self):
        conference = self.get_object()
        if self.request.user.username == conference.organizer.user.username:
            return True
        return False

@login_required
def feedback(request, pk):

    proposal = get_object_or_404(Proposal, pk=pk)

    if request.method == 'POST':
        f_form = FeedbackForm(request.POST, instance=proposal.feedback)
        p_form = ProposalStatusForm(request.POST, instance=proposal.proposalstatus)

        if f_form.is_valid() and p_form.is_valid():
            f_form.save()
            p_form.save()
            return redirect('proposals:proposal-detail', pk=pk)

    else:
        f_form = FeedbackForm(instance=proposal.feedback)
        p_form = ProposalStatusForm(instance=proposal.proposalstatus)

    context = {
        'f_form': f_form,
        'p_form': p_form
    }

    return render(request, 'events/feedback.html', context)
