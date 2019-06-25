import operator
import copy
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import SearchForm
from django.contrib.auth import get_user_model
from users.models import Speaker
from django.contrib.auth.decorators import login_required, user_passes_test

from proposals.models import Proposal
from users.models import Speaker
from proposals.forms import BulkSubmit

User = get_user_model()

# Create your views here.

def HomePageView(request):
    return render(request, "home/home.html")

def check_for_organizer(user):
    return user.is_organizer

@login_required
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

def leaderboard(request):
    points = []
    x = {'speaker':None, 'score_for_accepted':0, 'score_for_submission':0}
    users = Speaker.objects.all()
    for user in users:
        x['speaker'] = user
        proposal_submissions = user.proposal_set.all().filter(status='published')
        x['score_for_submission'] = proposal_submissions.count()
        for i in proposal_submissions:
                if i.proposalstatus.proposal_status == 'accepted':
                    x['score_for_accepted'] += 1
        points.append(x)
        x = {'speaker':None, 'score_for_accepted':0, 'score_for_submission':0}

    sort_by_submissions = copy.deepcopy(points)
    sort_by_submissions.sort(key=operator.itemgetter('score_for_submission'), reverse=True)
    print('=======================================')
    print(sort_by_submissions)
    print('=======================================')
    sort_by_accepted = copy.deepcopy(points)
    sort_by_accepted = sort_by_accepted.sort(key=operator.itemgetter('score_for_accepted'), reverse=True)

    return render(request, 'home/leaderboard.html', context={ 'q':sort_by_submissions })




    # if request.method == 'POST':
    #     x = dict(request.POST).get('proposal_list')
    #     for i in x:
    #         m = Proposal.objects.get(slug=i)
    #         setattr(m, 'status', 'published')
    #         m.save()
    #     return redirect('http://localhost:8000/leaderboard/')
    # else:
    #     form = BulkSubmit(request.user)
    # context = {'form' : form }
    # return render(request, 'home/leaderboard.html', context)
