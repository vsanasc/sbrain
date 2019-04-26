from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import BaseModel

from .choices import CURRENCY_CHOICES

class ExpenseCategory(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
            max_length=100
        )
    description = models.TextField(
            blank=True
        )
    order = models.SmallIntegerField()

    def __str__(self):
        return self.name


class ExpenseType(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
            ExpenseCategory,
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
    importance = models.PositiveSmallIntegerField(
        help_text='How much is important this expense for you. Min:1 - Max:10',
        default=5,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name
