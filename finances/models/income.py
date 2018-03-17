
from django.db import models

class Income(models.Model):
	name = models.CharField(max_length=60)
	value = models.PositiveIntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name