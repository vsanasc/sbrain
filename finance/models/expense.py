from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from core.models import BaseModel

from datetime import date as dat

from .choices import (
    METHOD_TYPE_CHOICES
)


class Expense(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'ExpenseType',
        on_delete=models.CASCADE,
        null=True
    )
    value = models.PositiveIntegerField()
    file = models.FileField(
        upload_to='income/',
        blank=True
    )
    date = models.DateField(
        default=dat.today
    )
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
        return '{} - {}'.format(
                self.type.name,
                self.value
            )
