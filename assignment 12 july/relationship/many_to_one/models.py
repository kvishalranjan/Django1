from django.db import models

# Create your models here.


class School(models.Model):
    name=models.CharField(max_length = 100)
    school_id=models.IntegerField()

    def __str__(self):
		    return str(self.school_id)

class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll_no = models.ForeignKey(School,on_delete = models.CASCADE)
	  
