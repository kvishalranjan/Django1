from django.db import models

# Create your models here.
gender_list=[('male','male'),('female','female')]
class Student_admission(models.Model): 
    fullname = models.CharField(max_length=40,default="")
    gender = models.CharField(choices=gender_list,max_length=10,default="male")
    age = models.IntegerField(default=0)
    dateofbirth = models.CharField(max_length=40,default="")
    city = models.CharField(max_length=40,default="")
    phone = models.IntegerField(default=0)
    is_verify = models.BooleanField(default=False)