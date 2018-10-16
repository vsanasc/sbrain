from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel

from django.utils import timezone

class Date(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    resume = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    stars = models.PositiveSmallIntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def total_notes(self):
        return self.smallnote_set.count()

    def total_cycles(self):
        cycles = 0
        for i in self.dedication_set.all():
            cycles += i.cycle

        return cycles

    def total_dedication(self):
        minutes = 0
        for i in self.dedication_set.all():
            minutes += i.cycle * i.time

        return minutes

    def proficiency_resume(self):
        cycles = self.total_cycles()
        minutes = self.total_dedication()
        time = round(float(minutes / 60), 1)
        return "cycles: {} | time: {}H".format(cycles, time)

    def proficiency_status(self):
        notes = self.total_notes()
        dedication = self.total_dedication()

        if notes > 2 and dedication >= 120:
            return '✅'
        
        if notes > 0 and dedication >= 30:
            return '⚠️'
        
        return '❌'



    def __str__(self):
        return self.date.strftime('%Y-%m-%d')
