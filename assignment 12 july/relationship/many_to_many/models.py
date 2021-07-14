from django.db import models

# Create your models here.
class Supplier(models.Model):
	supplier_name = models.CharField(max_length = 100)
	supplier_address = models.CharField(max_length = 300)
	
	def __str__(self):
		return str(self.supplier_name)

class Product(models.Model):
	product_desc = models.TextField(max_length = 300)	
	product_name = models.ManyToManyField(Supplier)