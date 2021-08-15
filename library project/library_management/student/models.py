from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20,default="")
    last_name = models.CharField(max_length=20,default="")
    DOB = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    contactno = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='student/photo/', null=True, blank=True)
    



