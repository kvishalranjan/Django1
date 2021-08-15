from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from datetime import datetime,timedelta,date


def student(request):
    if request.user.is_authenticated:
        
        return render(request,'student.html')

def studentsignup(request):
    form1=forms.StudentUserForm()
    
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        
        if form1.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            
        return HttpResponseRedirect('studentlogin')
    return render(request,'studentsignup.html',context=mydict)




def issuedbookbystudent(request):
    student=models.Student.objects.filter(user_id=request.user.id)
    issuedbook=models.IssuedBook.objects.filter(enrollment=student[0].enrollment)

    li1=[]

    li2=[]
    for ib in issuedbook:
        books=models.Book.objects.filter(isbn=ib.isbn)
        for book in books:
            t=(request.user,student[0].enrollment,student[0].branch,book.name,book.author)
            li1.append(t)
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
        t=(issdate,expdate,fine)
        li2.append(t)

    return render(request,'viewissuedbookbystudent.html',{'li1':li1,'li2':li2})

def studentlogin(request):
    if request.user.is_authenticated:
        return render(request,'studentafterlogin.html')