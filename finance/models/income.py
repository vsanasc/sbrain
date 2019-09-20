
from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel

from datetime import date as dat


class Income(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'IncomeType',
        on_delete=models.CASCADE,
        null=True
    )
    value = models.PositiveIntegerField()
    file = models.FileField(upload_to='income/', blank=True)
    date = models.DateField(default=dat.today)
    

    def __str__(self):
        return self.type.name if self.type else 'none'
