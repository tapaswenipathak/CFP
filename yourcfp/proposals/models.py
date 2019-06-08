from django.db import models
from django.contrib.auth import get_user_model
from events.models import Conference
from users.models import Speaker, Organizer
User = get_user_model()

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

REVIEW_STATUS = (
    ('to_be_reviewed', 'Is yet to be reviewed'),
    ('under_review', 'Being Reviewed'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected')
)

TYPES_OF_TALKS = (
    (30, 'Lightning talks'),
    (90, 'A session'),
    (180, 'A tutorial')
)

class Proposal(models.Model):
    author = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    name = models.ForeignKey(Conference, on_delete=models.CASCADE)
    outline = models.CharField(max_length=100, default=None)
    pitch = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,  default='draft')
    objects = models.Manager()
    talktime = models.IntegerField(choices=TYPES_OF_TALKS, default=30)
    published = PublishedManager()

    def __str__(self):
        return f'{self.author}\'s {self.name} proposal'

class ProposalStatus(models.Model):
    proposal_status = models.CharField(max_length=20, choices=REVIEW_STATUS,  default='to_be_reviewed')
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

class Feedback(models.Model):
    feedback_text = models.TextField()
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.proposal.author}'s {self.proposal.name} review"
