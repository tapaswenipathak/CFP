from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def HomePageView(request):
    x=request.user
    print(type(x.username))
    return render(request, "home/home.html")
