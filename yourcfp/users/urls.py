from django.urls import path, reverse_lazy
from .views import OrganizerRegisterView, SpeakerRegisterView

app_name = 'users'
urlpatterns = [
    path('register-as-organizer/', OrganizerRegisterView.as_view(), name='register-as-organizer'),
    path('register-as-speaker/', SpeakerRegisterView.as_view(), name='register-as-speaker'),
]
