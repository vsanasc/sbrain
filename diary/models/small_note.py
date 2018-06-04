from django.contrib.auth.models import User
from django.db import models

from core.model import BaseModel

class SmallNote(BaseModel):
    date = models.ForeignKey(
        'Date',
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self):
        return self.text
