from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def HomePageView(request):
    return render(request, "home/home.html")
