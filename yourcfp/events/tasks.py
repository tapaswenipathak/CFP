from celery import task
from django.core.mail.message import EmailMessage
from django.conf import settings
import os

@task
def mail_ics_file(file_name, to):

    message = EmailMessage()
    message.from_email = settings.EMAIL_HOST_USER
    message.to = [to]
    message.subject = 'Add this event to you Calendar'
    message.attach_file(file_name)
    message.send()
