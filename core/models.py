from django.contrib.auth.models import User
from django.db import models

from .choices import STATUS_CHOICES

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        abstract = True

class Tag(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name