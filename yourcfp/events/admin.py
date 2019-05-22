from django.contrib import admin
from .models import Event, Organizer

# Register your models here.
admin.site.register(Organizer)
admin.site.register(Event)
