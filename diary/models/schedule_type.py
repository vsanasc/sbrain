from django.contrib.auth.models import User
from django.db import models

from core.model import BaseModel


class TypeSchedule(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name