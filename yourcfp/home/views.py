from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import SearchForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def HomePageView(request):
    return render(request, "home/home.html")

def user_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = User.objects.filter(username__icontains=query)

    return render(request, 'home/search.html',{'form': form,'query': query,'results': results})
