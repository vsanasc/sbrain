from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


class Schedule(BaseModel):
    date = models.ForeignKey(
        'Date',
        on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        'TypeSchedule',
        on_delete=models.CASCADE
    )
    time = models.TimeField()

    def __str__(self):
        return self.time.strftime('%H:%M:%s')