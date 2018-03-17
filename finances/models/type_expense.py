from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CategoryTypeExpense(models.Model):
	name = models.CharField(
			max_length=100
		)
	description = models.TextField(
			blank=True
		)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name


class TypeExpense(models.Model):
	category = models.ForeignKey(
			CategoryTypeExpense, 
			on_delete=models.CASCADE
		)
	name = models.CharField(
			max_length=100
		)
	description = models.TextField(
			blank=True
		)
	rank = models.PositiveSmallIntegerField(
		default=5,
		validators=[MaxValueValidator(10), MinValueValidator(1)]
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name


