from django.db import models

# Create your models here.

class Aadhar(models.Model):
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.reg_no)

class Person(models.Model):
	identity = models.OneToOneField(Aadhar, on_delete = models.CASCADE, primary_key = True)
	name = models.CharField(max_length = 100)
