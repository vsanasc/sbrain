
from django.db import models
from django.contrib.auth.models import User

from datetime import date as dat
from .choices import CURRENCY_CHOICES


class Income(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60)
    value = models.PositiveIntegerField()
    file = models.FileField(upload_to='income/', blank=True)
    date = models.DateField(default=dat.today)
    currency = models.CharField(
        max_length=3,
        default='USD',
        choices=CURRENCY_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
