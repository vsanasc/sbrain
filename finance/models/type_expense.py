from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import BaseModel

class CategoryTypeExpense(BaseModel):
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


    def __str__(self):
        return self.name


class TypeExpense(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
            CategoryTypeExpense,
            on_delete=models.CASCADE
        )
    name = models.CharField(
            max_length=100
        )
    note = models.CharField(
            max_length=200,
            blank=True
        )
    importance = models.PositiveSmallIntegerField(
        help_text='How much is important this expense for you. Min:1 - Max:10',
        default=5,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name
