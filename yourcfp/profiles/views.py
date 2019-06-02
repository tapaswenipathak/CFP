from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponse

User = get_user_model()

# Create your views here

# @login_required
# def profile(request):
#     username = request.user
#     speaker_type = request.user.is_speaker
#     detail = None
#
#     if request.method == "POST" and username == request.user and speaker_type:
#         user = User.objects.get(pk=username.id)
#         detail = Profile.objects.filter(user=user).exists()
#         if detail:
#             detail = Profile.objects.get(user=user)
#             detail_form = ProfileForm(request.POST, instance=detail)
#             if detail_form.is_valid():
#                 detail = detail_form.save()
#                 return redirect(reverse('profiles:profile'))
#         else:
#             user = User.objects.get(pk=username.id)
#             detail_form = ProfileForm(request.POST)
#             if detail_form.is_valid():
#                 detail_form = detail_form.save(commit=False)
#                 detail_form.user = user
#                 detail_form.save()
#                 return redirect('profiles:profile')
#
#     elif request.method == "GET" and speaker_type:
#         user = User.objects.get(pk=username.id)
#         detail = Profile.objects.filter(user=user).exists()
#         if detail:
#             form = ProfileForm()
#             return render(request, 'profiles/userprofile.html', {'form': form})
#         else:
#             form = ProfileForm()
#             return render(request, 'profiles/userprofile.html', {'form': form})
#
# def profile_detail(request, user_name):
#     user = User.objects.filter(username=user_name).exists()
#     if user:
#         user = User.objects.get(username=user_name)
#         profile = Profile.objects.filter(user=user).exists()
#         if profile:
#             profile = Profile.objects.get(user=user)
#             context = {
#                 'blog_url':profile.blog_url,
#                 'location':profile.location,
#                 'twitter_handle':profile.twitter_handle,
#                 'biography':profile.bio
#             }
#             return render(request, 'profiles/profile.html', context)
#         else:
#             return HttpResponse('Does not exist')
#     else:
#         return HttpResponse('User does not exist')



@login_required
def profile(request):
    print(request.user.profile.bio)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profiles:profile')

    else:
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'form': profile_form
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
