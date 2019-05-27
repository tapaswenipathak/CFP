from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse

from .models import Conference
from .forms import ConferenceForm

User = get_user_model()

# Create your views here

class ConferenceList(ListView):
    model = Conference

class ConferenceDetailView(DetailView):
    model = Conference

class ConferenceCreateView(LoginRequiredMixin, CreateView):
    model = Conference
    fields = ['name', 'description', 'start_date', 'end_date', 'venue', 'twitter_id']
    success_url=reverse_lazy('events:conference-list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class ConferenceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Conference
    fields = ['name', 'description', 'start_date', 'end_date', 'venue', 'twitter_id']
    success_url=reverse_lazy('events:conference-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        conference = self.get_object()
        if self.request.user == conference.organizer:
            return True
        return False
