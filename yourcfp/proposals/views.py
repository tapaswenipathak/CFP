from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import ProposalForm
from .models import Proposal
from events.models import Conference

# Create your views here.

class ProposalCreateView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Proposal
    fields = ['name', 'content', 'status']
    success_url = reverse_lazy('proposals:proposal-list')
    permission_required = 'proposals.add_proposal'

    def form_valid(self, form):
        form.instance.author = self.request.user.speaker
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.is_speaker:
            return True
        return False

class UserProposalListView(ListView):
    model = Proposal
    def get_queryset(self):
        return Proposal.objects.filter(author=self.request.user.speaker)

class ProposalDetailView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Proposal
    permission_required = 'proposals.view_proposal'

    def test_func(self):
        proposal = self.get_object()
        if self.request.user.is_speaker:
            if proposal.author == self.request.user.speaker:
                return True
        elif proposal.name.organizer.user == self.request.user:
            return True
        return False

class ProposalUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Proposal
    fields = ['name', 'content', 'status']
    success_url = reverse_lazy('proposals:proposal-list')
    permission_required = 'proposals.change_proposal'

    def form_valid(self, form):
        form.instance.author = self.request.user.speaker
        return super().form_valid(form)

    def test_func(self):
        proposal = self.get_object()
        if self.request.user.speaker == proposal.author:
            return True
        return False
