from django.db import models

from core.model import BaseModel


class Phrase(BaseModel):
    text = models.CharField(max_length=100)
    lang = models.CharField(max_length=2)
    variation = models.CharField(max_length=3)


class PhraseAudio(BaseModel):
    phrase = models.ForeignKey('Phrase', on_delete=models.CASCADE)
    path_file = models.CharField(max_length=100)
    robotic = models.BooleanField(default=True)
    robotic_speed = models.SmallIntegerField()


class RelationPhrase(BaseModel):
    episode = models.ForeignKey('Episode', on_delete=models.CASCADE)
    phrase = models.ForeignKey('Phrase', on_delete=models.CASCADE)
    order = models.SmallIntegerField()
