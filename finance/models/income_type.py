from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel
from .choices import CURRENCY_CHOICES


class IncomeType(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100
    )
    note = models.CharField(
        max_length=200,
        blank=True
    )
    currency = models.CharField(
        max_length=3,
        default='USD',
        choices=CURRENCY_CHOICES
    )

    def __str__(self):
        return self.name