from django.urls import path
from .views import profile, profile_detail

app_name = 'profiles'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/<slug:slug>', profile_detail, name='profile_detail')
]
