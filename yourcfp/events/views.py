from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Conference
from .forms import ConferenceForm, FeedbackForm, ProposalStatusForm, ConferenceDashboardForm
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
    fields = ['name', 'description', 'start_date', 'end_date', 'venue', 'twitter_id', 'topic_tags']
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
    fields = ['name', 'description', 'start_date', 'end_date', 'venue', 'twitter_id', 'topic_tags']
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

def is_reviewer(user):
    return user.is_organizer

@login_required
@permission_required(['proposals.add_proposalstatus', 'proposals.add_feedback'], raise_exception=True)
@user_passes_test(is_reviewer)
def feedback(request, pk, slug):

    proposal = get_object_or_404(Proposal, pk=pk, status='published')
    if proposal.name.organizer == request.user.organizer:
        if request.method == 'POST':
            f_form = FeedbackForm(request.POST, instance=proposal.feedback)
            p_form = ProposalStatusForm(request.POST, instance=proposal.proposalstatus)

            if f_form.is_valid() and p_form.is_valid():
                f = f_form.save(commit=False)
                f.proposal = proposal
                f.reviewer = request.user.organizer
                f.save()
                p = p_form.save(commit=False)
                p.proposal = proposal
                p.reviewer = request.user.organizer
                p.save()
                return redirect('proposals:proposal-detail', pk=pk, slug=slug)

        else:
            f_form = FeedbackForm(instance=proposal.feedback)
            p_form = ProposalStatusForm(instance=proposal.proposalstatus)

        context = {
            'f_form': f_form,
            'p_form': p_form
        }

        return render(request, 'events/feedback.html', context)
    return HttpResponseForbidden('<h1>403 forbidden<h1/>')

def check_for_organizer(user):
    return user.is_organizer

@login_required
@user_passes_test(check_for_organizer)
def conference_dashboard(request, pk, slug):
    conference = Conference.objects.get(id=pk)
    if request.user.organizer == conference.organizer:
        form = ConferenceDashboardForm()
        context = {
            'proposals' : [],
            'form' : form
        }
        proposals = conference.proposal_set.all()
        context['proposals'] = proposals
        options_list = ['accepted', 'rejected', 'all', 'pending_reviews']
        display_list = []

        if request.method == 'POST':
            selected_option = dict(request.POST).get('options')

            if selected_option[0] == 'accepted':
                for i in proposals:
                    if i.proposalstatus.proposal_status == 'accepted':
                        display_list.append(i)
                context['proposals'] = display_list
                return render(request, 'events/conference_dashboard.html', context)

            if selected_option[0] == 'rejected':
                for i in proposals:
                    if i.proposalstatus.proposal_status == 'rejected':
                        display_list.append(i)
                context['proposals'] = display_list
                return render(request, 'events/conference_dashboard.html', context)

            if selected_option[0] == 'all':
                for i in proposals:
                        display_list.append(i)
                context['proposals'] = display_list
                return render(request, 'events/conference_dashboard.html', context)

            if selected_option[0] == 'pending_reviews':
                for i in proposals:
                    if i.proposalstatus.proposal_status == 'to_be_reviewed':
                        display_list.append(i)
                context['proposals'] = display_list
                return render(request, 'events/conference_dashboard.html', context)

        else:
            context['form'] = form
        return render(request, 'events/conference_dashboard.html', context)
    else:
        return HttpResponseForbidden('<h1>403 forbidden<h1/>')
