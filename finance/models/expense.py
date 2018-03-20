from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext as _
from datetime import date as dat

from .choices import (
    CURRENCY_CHOICES,
    METHOD_TYPE_CHOICES
)


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'TypeExpense',
        on_delete=models.CASCADE
    )
    value = models.PositiveIntegerField()
    file = models.FileField(
        upload_to='income/',
        blank=True
    )
    date = models.DateField(
        default=dat.today
    )
    currency = models.CharField(
        max_length=3,
        default='USD',
        choices=CURRENCY_CHOICES
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(
                self.type.name,
                self.value
            )
