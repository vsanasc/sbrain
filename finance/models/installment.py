from django.db import models

from core.model import BaseModel


class Installment(BaseModel):
    name = models.CharField(max_length=60)

