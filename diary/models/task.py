from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


class Task(BaseModel):
    date = models.ForeignKey(
        'Date',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'TypeTask',
        on_delete=models.CASCADE
    )
    observation = models.CharField(
        max_length=200,
        blank=True
    )
