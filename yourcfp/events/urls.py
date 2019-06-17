from django.urls import path
from .views import (ConferenceList, UserConferenceList, ConferenceDetailView,
                    ConferenceCreateView, ConferenceUpdateView, ConferenceProposalListView)
from proposals.views import ProposalCreateView

app_name = 'events'

urlpatterns = [
    path('conference-list/', ConferenceList.as_view(), name='conference-list'),
    path('conference-proposal-list/<int:pk>/<slug:slug>/', ConferenceProposalListView.as_view(), name='conference-proposal-list'),
    path('my-conference-list/', UserConferenceList.as_view(), name='user-conference-list'),
    path('conference/<int:pk>/<slug:slug>/', ConferenceDetailView.as_view(), name='conference-detail'),
    path('conference/<int:pk>/<slug:slug>/update', ConferenceUpdateView.as_view(), name='conference-update'),
    path('conference/new', ConferenceCreateView.as_view(), name='conference-create'),

    #propsosal create
    path('conference/<int:pk>/<slug:slug>/proposal/create', ProposalCreateView.as_view(), name='proposal-create'),
]
