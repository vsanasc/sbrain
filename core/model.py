from django.db import models

from .choices import STATUS_CHOICES

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    class Meta:
        abstract = True
