from django.db import models

from core.model import BaseModel


class Producer(BaseModel):
    name = models.CharField(max_length=50)


class Production(BaseModel):
    name = models.CharField(max_length=50)


class Season(BaseModel):
    producer = models.ForeignKey('Production', on_delete=models.CASCADE)


class Episode(BaseModel):
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
