# Generated by Django 2.0 on 2018-06-11 02:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0010_task_observation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role',
            new_name='GeneralType',
        ),
    ]
