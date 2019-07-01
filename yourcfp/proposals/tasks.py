import datetime

from django.core.mail import send_mail
from celery import Celery
from celery import task
from django.conf import settings

from proposals.models import Proposal

@task
def proposal_remainder():
    proposals = Proposal.objects.all().filter(status='draft')

    for proposal in proposals:
        if proposal.name.start_date < datetime.date.today():
            subject = 'Proposal submission remainder'
            message = f'Dear {proposal.author},\nThe deadline for proposal {proposal.title} submission is here.Submit your proposal for conference {proposal.name.name}.'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [proposal.author.user.email])
