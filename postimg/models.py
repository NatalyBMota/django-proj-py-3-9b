from typing import Any
from django.db import models

# Create your models here.
class Postimg (models.Model):
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=1000)
	image=models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title