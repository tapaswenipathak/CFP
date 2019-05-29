from django.urls import path
from .views import proposal_view, ProposalListView

app_name = 'proposals'

urlpatterns = [
    path('', proposal_view, name='proposal'),
    path('proposal-list', ProposalListView.as_view(), name='proposal-list'),
]
