from django.db import models


class UserApp(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=40)


	def __unicode__(self):
		return '{} {}'.format(self.first_name, self.last_name)