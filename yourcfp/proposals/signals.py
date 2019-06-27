from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Proposal, Feedback, ProposalStatus

User = get_user_model()

@receiver(post_save, sender=Proposal)
def create_feedback_instance(sender, instance, created, **kwargs):
    if created:
        print('--------------------')
        print(instance)
        print('--------------------')
        ProposalStatus.objects.create(proposal=instance,
                                      reviewer = instance.name.organizer,
                                      proposal_status='to_be_reviewed')

        Feedback.objects.create(proposal=instance,
                                reviewer=instance.name.organizer,
                                feedback_text='Is to be updated')

@receiver(post_save, sender=Proposal)
def save_feedback_instance(sender, instance, **kwargs):
    instance.proposalstatus.save()
    instance.feedback.save()
