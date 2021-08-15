from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from datetime import datetime,timedelta,date
from .forms import *


def adminclick(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'adminclick.html')

def librarian(request):
    
    form = LibrarianSignupForm()
    if request.method=='POST':
        form = LibrarianSignupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            
    return render(request, 'adminclick.html', locals())

def adminsignup(request):
    form=AdminSignupForm()
    if request.method=='POST':
        form=AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',{'form':form})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()



def adminafterlogin(request):
    if is_admin(request.user):
        return render(request,'adminafterlogin.html')
    else:
        return render(request,'studentafterlogin.html')

def addbook(request):
    #now it is empty book form for sending to html
    form=forms.BookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bookadded.html')
    return render(request,'addbook.html',{'form':form})

def viewbook(request):
    books=models.Book.objects.all()
    return render(request,'viewbook.html',{'books':books})

def issuebook(request):
    form=forms.IssuedBookForm()
    print(form)
    # return HttpResponse('hi')
    # if request.method=='POST':
    #     #now this form have data from html
    #     form=forms.IssuedBookForm(request.POST)
    #     if form.is_valid():
    #         obj=models.IssuedBook()
    #         obj.enrollment=request.POST.get('enrollment1')
    #         obj.isbn=request.POST.get('isbn1')
    #         obj.save()
    #         return render(request,'bookissued.html')
    return render(request,'issuebook.html',{'form':form})

def issuedbook(request):
    issuedbooks=models.IssuedBook.objects.all()
    li=[]
    for ib in range(0,len(issuedbooks)):
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10


        books=list(models.Book.objects.filter(isbn=ib.isbn))
        students=list(models.Student.objects.filter(enrollment=ib.enrollment))
        i=0
        for l in range(0,len(books)):
            t=(students[i].get_name,students[i].enrollment,books[i].name,books[i].author,issdate,expdate,fine)
            i=i+1
            li.append(t)

    return render(request,'viewissuedbook.html',{'li':li})


def adminlogin(request):
    
    if request.user.is_authenticated:
        return render(request,'adminafterlogin.html')
    else:
        return render(request,'adminlogin.html') 


def viewstudent(request):
    students=models.Student.objects.all()
    return render(request,'viewstudent.html',{'students':students})

def logout(request):
    request.session.flush()
    logout(request)
    return render(request,'adminlogin.html')


def login(request):
    if request.method == 'POST':
        data = request.POST
        librarianname = data['librarianname']
        password = data['pass']
        # User.objects.filter(username=username,password=password)
        librarian = authenticate(username=librarianname, password=password)
        if librarian:
            login(request, librarian)
            messages.success(request, f"Welcome, {librarianname}")
            if librarian.is_student:
                return redirect("librarian:adminsignup")
            else:
                return redirect("librarian:adminclick")
        else:
            messages.error(request, 'Please Provide Valid Username / Password')
    if request.user.is_authenticated:
        return redirect('librarian:adminsignup')
    return render(request, 'login.html')
