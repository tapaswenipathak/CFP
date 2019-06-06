# Generated by Django 2.2 on 2019-05-28 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_auto_20190528_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Conference'),
        ),
    ]