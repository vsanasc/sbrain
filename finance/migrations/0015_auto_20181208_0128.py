# Generated by Django 2.1.4 on 2018-12-08 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0014_auto_20181208_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.ExpenseType'),
        ),
    ]
