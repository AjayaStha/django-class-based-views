from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	mobile = models.CharField(max_length=50)
	email = models.EmailField(max_length=30)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name