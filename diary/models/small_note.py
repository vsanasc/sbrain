from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

from core.models import BaseModel

class SmallNote(BaseModel):
    date = models.ForeignKey(
        'Date',
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE
    )
    text = HTMLField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.text
