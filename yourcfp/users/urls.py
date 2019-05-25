from django.urls import path, reverse_lazy
from .views import OrganizerRegisterView, SpeakerRegisterView, SpeakerSuccess, OrganizerSuccess

app_name = 'users'
urlpatterns = [
    path('organizer_success/', OrganizerSuccess.as_view(), name='organizer-success'),
    path('speaker_success/', SpeakerSuccess.as_view(), name='speaker-success'),
    path('register-as-organizer/', OrganizerRegisterView.as_view(), name='register-as-organizer'),
    path('register-as-speaker/', SpeakerRegisterView.as_view(), name='register-as-speaker'),
]
