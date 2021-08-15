from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('adminclick')
    return render(request,'home.html')