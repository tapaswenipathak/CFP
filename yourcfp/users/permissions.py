from django.contrib.auth.models import Permission, Group

SPEAKER_PERMISSIONS =  [
		Permission.objects.get(codename='add_proposal'),
		Permission.objects.get(codename='change_proposal'),
		Permission.objects.get(codename='view_proposal'),
		Permission.objects.get(codename='delete_proposal')
	]

ORGANIZER_PERMISSIONS =  [
		Permission.objects.get(codename='add_conference'),
        Permission.objects.get(codename='change_conference'),
        Permission.objects.get(codename='view_conference'),
        Permission.objects.get(codename='delete_conference'),
        Permission.objects.get(codename='view_proposal')
	]

def set_speaker_permission(user):
	group,created = Group.objects.get_or_create(name='speaker')
	if not created:
		for i in group.permissions.all():
			group.permissions.remove(i)

	for i in SPEAKER_PERMISSIONS:
		group.permissions.add(i)

	user.groups.add(group)

def set_organizer_permission(user):
	group,created = Group.objects.get_or_create(name='organizer')
	if not created:
		for i in group.permissions.all():
			group.permissions.remove(i)

	for i in ORGANIZER_PERMISSIONS:
		group.permissions.add(i)

	user.groups.add(group)
