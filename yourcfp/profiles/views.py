from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from proposals.models import Proposal, ProposalStatus
from .models import Profile
from .forms import ProfileForm, DashboardForm
from django.http import HttpResponse
from proposals.forms import BulkSubmit

User = get_user_model()

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profiles:profile')

    else:
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'form': profile_form,
        'user':request.user
    }

    return render(request, 'profiles/userprofile.html', context)

def profile_detail(request, slug):
    user = User.objects.filter(slug=slug).exists()
    if user:
        user = User.objects.get(slug=slug)
        profile = Profile.objects.get(user=user)
        context = {
            'blog_url':profile.blog_url,
            'location':profile.location,
            'twitter_handle':profile.twitter_handle,
            'biography':profile.bio
        }
        return render(request, 'profiles/profile.html', context)
    else:
        return HttpResponse('User does not exist')

def speaker_dashboard(request):
    form = DashboardForm()
    context = {
        'proposals' : [],
        'form' : form
    }
    proposals = Proposal.objects.filter(author=request.user.speaker)
    context['proposals'] = proposals
    options_list = ['accepted' , 'rejected', 'draft', 'published']
    display_list = []
    if request.method == 'POST':

        selected_option = dict(request.POST).get('options')

        if selected_option[0] == 'accepted':
            print('accepted')
            for i in proposals:
                if i.proposalstatus.proposal_status == 'accepted':
                    display_list.append(i)
            context['proposals'] = display_list
            return render(request, 'profiles/dashboard.html', context)

        if selected_option[0] == 'rejected':
            for i in proposals:
                if i.proposalstatus.proposal_status == 'rejected':
                    display_list.append(i)
            context['proposals'] = display_list
            return render(request, 'profiles/dashboard.html', context)

        if selected_option[0] == 'draft':
            for i in proposals:
                if i.status == 'draft':
                    display_list.append(i)
            context['proposals'] = display_list
            return render(request, 'profiles/dashboard.html', context)

        if selected_option[0] == 'published':
            for i in proposals:
                if i.status == 'published':
                    display_list.append(i)
            context['proposals'] = display_list
            return render(request, 'profiles/dashboard.html', context)

    else:
        context['form'] = form
    return render(request, 'profiles/dashboard.html', context)

@login_required
def bulk_submit(request):
    if request.method == 'POST':
        x = dict(request.POST).get('proposal_list')
        for i in x:
            m = Proposal.objects.get(slug=i)
            setattr(m, 'status', 'published')
            m.save()
        return redirect(reverse('profiles:dashboard'))
    else:
        form = BulkSubmit(request.user)
    context = {'form' : form }
    return render(request, 'profiles/bulk_submit_form.html', context)
