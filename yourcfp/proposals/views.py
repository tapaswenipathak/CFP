from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse

from .forms import ProposalForm
from .models import Proposal
# Create your views here.
@login_required
def proposal_view(request):
    if request.method == 'POST':
        proposal_form = ProposalForm(request.POST)
        if proposal_form.is_valid():
            proposal_form.save()
            return redirect('home:index')
    else:
        profile_form = ProposalForm()
    context = {
        'form': profile_form
        }
    return render(request, 'proposals/proposal.html', context)

class ProposalListView(ListView):
    model = Proposal

class ProposalDetailView(DetailView):
    model = Proposal
