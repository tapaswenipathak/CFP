from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView


from .forms import OrganizerSignUpForm, SpeakerSignUpForm
from .models import User

# Create your views here

class OrganizerRegisterView(CreateView):
    model = User
    form_class = OrganizerSignUpForm
    template_name = 'users/organizer_register_form.html'
    success_url = reverse_lazy('users:organizer-success')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'organizer'
        return super().get_context_data(**kwargs)

class SpeakerRegisterView(CreateView):
    model = User
    form_class = SpeakerSignUpForm
    template_name = 'users/speaker_register_form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'speaker'
        return super().get_context_data(**kwargs)

class OrganizerSuccess(TemplateView):
    template_name = "users/organizer_redirect.html"

class SpeakerSuccess(TemplateView):
    template_name = "users/speaker_redirect.html"
