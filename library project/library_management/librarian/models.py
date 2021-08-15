from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.

class Book(models.Model):
    catchoice = [
        ('education','Education'),
        ('entertainment','Entertainment'),
        ('comics','Comics'),
        ('biography','Biography'),
        ('history','History'),
    ]
    bookname=models.CharField(max_length=30)
    authorname=models.CharField(max_length=40)
    isbn=models.PositiveBigIntegerField()
    category=models.CharField(max_length=30, choices=catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+"]"

def get_expiry():
    return datetime.today()+timedelta(15)
class IssuedBook(models.Model):
        # enrollment=[(student.enrollment,str(student.get_name)+'['+str(student.enrollment)+']')for student in Student.objects.all()]
        enrollment=models.CharField(max_length=30)
        # isbn=[(str(book.isbn),book.name+'['+str(book.isbn)+']')for book in Book.objects.all()]
        isbn=models.CharField(max_length=30)
        issuedate=models.DateField(auto_now=True)
        expirydate=models.DateField(default=get_expiry())
        def __str__(self):
            return self.enrollment

class Librarian(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    DOB = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contactno = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='librarian/photo/', null=True, blank=True)

class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    
    def get_name(self):
        return self.user.first_name
    
    def getuserid(self):
        return self.user.id

class Student(models.Model):
    first_name = models.CharField(max_length=20,default="")
    last_name = models.CharField(max_length=20,default="")
    DOB = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    contactno = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='student/photo/', null=True, blank=True)
    
         
