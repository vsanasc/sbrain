from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel

from .choices import METHOD_TYPE_CHOICES


class Installment(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60)
    start = models.DateField()
    number = models.PositiveSmallIntegerField()
    value = models.PositiveIntegerField()
    method = models.PositiveSmallIntegerField(
        choices=METHOD_TYPE_CHOICES
    )
    credit_card = models.ForeignKey(
        'CreditCard',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
