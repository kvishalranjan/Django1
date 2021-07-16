from django.db import models

# Create your models here.
gender_list=[('male','male'),('female','female')]
class Person(models.Model):
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    salary = models.FloatField()
    gender = models.CharField(choices=gender_list,max_length=10,default="male")
    is_verify = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} | {self.first_name} {self.last_name} | {self.gender} | {self.age} | {self.email} | {self.is_verify}"

technology_choice = [
    ('artificial_inteligence', 'artificial_inteligence'),
    ('data_scientist', 'data_scientist'),
    ('blockchain', 'blockchain'),
    ('cloud_computing', 'cloud_computing'),
    ('cyber_security', 'cyber_security')] 

class Technology(models.Model):
    technology = models.CharField(choices=technology_choice, max_length=50, default='cyber_security')
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=50,default="")    
