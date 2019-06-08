from django.contrib import admin
from .models import Proposal, ProposalStatus, Feedback

# Register your models here.
admin.site.register(Proposal)
admin.site.register(ProposalStatus)
admin.site.register(Feedback)
