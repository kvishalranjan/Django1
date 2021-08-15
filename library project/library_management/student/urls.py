from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'student'

urlpatterns = [
    
    path('student', student,name='student'),
    path('studentsignup', studentsignup,name='studentsignup'),
    path('studentlogin', studentlogin,name='studentlogin'),
    
    path('issuedbookbystudent', issuedbookbystudent,name='issuedbookbystudent'),
    path('viewissuedbookbystudent', issuedbookbystudent,name='viewissuedbookbystudent'),


   

]