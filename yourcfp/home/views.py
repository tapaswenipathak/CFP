from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import SearchForm
from django.contrib.auth import get_user_model
from users.models import Speaker
from django.contrib.auth.decorators import login_required, user_passes_test
User = get_user_model()

# Create your views here.

def HomePageView(request):
    return render(request, "home/home.html")

def check_for_organizer(user):
    return user.is_organizer

@login_required
@user_passes_test(check_for_organizer)
def user_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = list(User.objects.filter(username__icontains=query))

    for i in results:
        if i.is_organizer:
            results.remove(i)

    context = {
                'form': form,
                'query': query,
                'results': results
                }

    return render(request, 'home/search.html',context)
