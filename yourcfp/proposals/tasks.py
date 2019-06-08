from celery import task
from django.core.mail import send_mail
from .models import Proposal

@task
def propsal_remainder(proposal_id):
    proposal = Proposal.published.get(proposal_id)
    subject = 'Proposal no. {}'.format(proposal.id)
    message = 'Dear {},\nThe deadline for proposal submission is here\
                Submit your proposal for conference {}.'.format(Proposal.author,proposal.name.name)
    mail_sent = send_mail(subject,message,'admin@myshop.com',[proposal.author.user.email])
    return mail_sent
