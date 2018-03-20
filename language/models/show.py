from django.db import models

from .choices import STATUS_CHOICES


class Producer(models.Model):
    name = models.CharField(max_length=50)

    # extras
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)


class Production(models.Model):
    name = models.CharField(max_length=50)


class Season(models.Model):
    producer = models.ForeignKey('Production', on_delete=models.CASCADE)


class Episode(models.Model):
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    # extras
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
