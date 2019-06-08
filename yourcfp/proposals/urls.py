from django.urls import path
from .views import ProposalCreateView, UserProposalListView, ProposalDetailView, ProposalUpdateView
from events.views import feedback
app_name = 'proposals'

urlpatterns = [
    path('', ProposalCreateView.as_view(), name='proposal'),
    path('list', UserProposalListView.as_view(), name='proposal-list'),
    path('<int:pk>/', ProposalDetailView.as_view(), name='proposal-detail'),
    path('<int:pk>/feedback', feedback, name='proposal-feedback'),
    path('<int:pk>/update', ProposalUpdateView.as_view(), name='proposal-update')
]
