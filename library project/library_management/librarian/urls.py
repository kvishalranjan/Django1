from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views
app_name = 'librarian'


urlpatterns = [
    

    path('adminclick', adminclick,name='adminclick'),
    path('adminsignup', adminsignup,name='adminsignup'),
    path('adminlogin', adminlogin, name='adminlogin'),
    
    path('adminafterlogin', adminafterlogin,name='adminafterlogin'),
    path('logout/', logout,name='logout'),

    path('addbook', addbook,name='addbook'),
    path('viewbook', viewbook,name='viewbook'),
    path('issuebook', issuebook,name='issuebook'),
    path('issuedbook', issuedbook,name='issuedbook'),
    path('librarian', librarian,name='librarian'),
    path('viewstudent',viewstudent,name='viewstudent'),
    path('viewissuedbook', issuedbook,name='viewissuedbook'),
    
    
    
    

]
    
