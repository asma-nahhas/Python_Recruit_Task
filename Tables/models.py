from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Table(models.Model):
	name=models.CharField(max_length=200)
	created_at=models.DateTimeField(default=datetime.now,blank=True)
	def __str__(self):
		return self.name
	
