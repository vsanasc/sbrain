# Generated by Django 2.1.4 on 2018-12-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0017_auto_20181208_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensecategory',
            name='order',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
