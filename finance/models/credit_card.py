
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from core.models import BaseModel

from .choices import (
    TYPE_CREDIT_CARD_CHOICES,
    CURRENCY_CHOICES
)


class CreditCard(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CREDIT_CARD_CHOICES
    )
    limit = models.PositiveIntegerField()
    bill_day = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ]
    )
    currency = models.CharField(
        max_length=3,
        default='USD',
        choices=CURRENCY_CHOICES
    )

    def __str__(self):
        return self.name


class CreditCardBill(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    credit_card = models.ForeignKey(
            'CreditCard',
            on_delete=models.CASCADE
        )
    file = models.FileField(
        upload_to='bills/'
    )
    total = models.PositiveIntegerField()
    paid = models.DateTimeField()


    def __str__(self):
        return '{} {}'.format(
            self.total,
            self.paid
        )
