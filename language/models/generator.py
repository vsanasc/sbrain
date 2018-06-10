from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel

class Generator(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    repeat = models.SmallIntegerField()
    translate_repeat = models.SmallIntegerField()
    random = models.BooleanField()

    def __str__(self):
        return self.name
