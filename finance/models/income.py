
from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel

from datetime import date as dat
from .choices import CURRENCY_CHOICES


class Income(BaseModel):
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

    def __str__(self):
        return self.name
