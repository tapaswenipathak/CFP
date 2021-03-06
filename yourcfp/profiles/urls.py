from django.urls import path
from .views import profile, profile_detail, bulk_submit, speaker_dashboard

app_name = 'profiles'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/<slug:slug>', profile_detail, name='profile-detail'),
    path('draft-proposals/', bulk_submit, name='bulk_submit'),
    path('speaker/dashboard', speaker_dashboard, name='speaker-dashboard'),
]
