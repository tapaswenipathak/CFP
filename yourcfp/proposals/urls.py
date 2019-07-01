from django.urls import path
from .views import ProposalCreateView, UserProposalListView, ProposalDetailView, ProposalUpdateView
from events.views import feedback

app_name = 'proposals'

urlpatterns = [
    path('list', UserProposalListView.as_view(), name='proposal-list'),
    path('<int:pk>/<slug:slug>/', ProposalDetailView.as_view(), name='proposal-detail'),
    path('<int:pk>/<slug:slug>/feedback', feedback, name='proposal-feedback'),
    path('<int:pk>/<slug:slug>/update', ProposalUpdateView.as_view(), name='proposal-update')
]
