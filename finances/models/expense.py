from django.db import models

METHOD_TYPE = (
		(1, 'Cash'),
		(2, 'Credit Card'),
		(3, 'Check')
	)


class Expense(models.Model):
	type = models.ForeignKey(
			'TypeExpense',
			on_delete=models.CASCADE
		)
	value = models.PositiveIntegerField()
	method = models.PositiveSmallIntegerField(
			choices=METHOD_TYPE
		)
	credit_card = models.ForeignKey(
			'CreditCard',
			on_delete=models.CASCADE
		)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		values = (self.type.name, self.value)
		return '{} - {}'.format(values)
