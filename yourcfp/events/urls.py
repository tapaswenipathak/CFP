from django.urls import path
from .views import ConferenceList, ConferenceDetailView, ConferenceCreateView, ConferenceUpdateView

app_name = 'events'

urlpatterns = [
    path('conference-list/', ConferenceList.as_view(), name='conference-list'),
    path('conference/<int:pk>', ConferenceDetailView.as_view(), name='conference-detail'),
    path('conference/<int:pk>/update', ConferenceUpdateView.as_view(), name='conference-update'),
    path('conference/new', ConferenceCreateView.as_view(), name='conference-create')
]
