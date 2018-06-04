from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models

from core.model import BaseModel


class Date(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    resume = models.TextField(blank=True)
    date = models.DateField()
    stars = models.PositiveSmallIntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')
