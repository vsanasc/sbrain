from django.db import models

TYPE_CREDIT_CARD = (
		(1, 'Visa'),
		(2, 'Mastercard'),
		(3, 'American Express'),
		(4, 'Another'),
	)

class CreditCard(models.Model):
	name = models.CharField(max_length=50)
	type = models.PositiveSmallIntegerField(
			choices=TYPE_CREDIT_CARD
		)
	limit = models.PositiveIntegerField()
	bill_date = models.DateField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class CreditCardBill(models.Model):
	credit_card = models.ForeignKey(
			'CreditCard',
			on_delete=models.CASCADE
		)
	file = models.FileField(upload_to='bills/')
	total = models.PositiveIntegerField()
	paid = models.DateTimeField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
