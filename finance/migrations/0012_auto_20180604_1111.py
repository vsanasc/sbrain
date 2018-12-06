# Generated by Django 2.0 on 2018-06-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_auto_20180519_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytypeexpense',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='creditcardbill',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='expense',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='income',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='installment',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
        migrations.AlterField(
            model_name='typeexpense',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
    ]
