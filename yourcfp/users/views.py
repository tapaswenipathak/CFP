from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

# Create your views here

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/user_register_form.html'
    success_url = reverse_lazy('home:index')
