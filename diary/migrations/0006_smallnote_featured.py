# Generated by Django 2.0 on 2018-06-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_dedication_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='smallnote',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]