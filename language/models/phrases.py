from django.db import models

from .choices import STATUS_CHOICES


class Phrase(models.Model):
    text = models.CharField(max_length=100)
    lang = models.CharField(max_length=2)
    variation = models.CharField(max_length=3)

    # extras
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)


class PhraseAudio(models.Model):
    phrase = models.ForeignKey('Phrase', on_delete=models.CASCADE)
    path_file = models.CharField(max_length=100)
    robotic = models.BooleanField(default=True)
    robotic_speed = models.SmallIntegerField()

    # extras
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)


class RelationPhrase(models.Model):
    episode = models.ForeignKey('Episode', on_delete=models.CASCADE)
    phrase = models.ForeignKey('Phrase', on_delete=models.CASCADE)
    order = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
