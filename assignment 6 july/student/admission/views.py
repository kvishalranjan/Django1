from django.shortcuts import render
from django.http import HttpResponse
from .forms import Student_admissionForm

# Create your views here.

def home(request):
    form = Student_admissionForm()
    if request.method=='POST':
        form = Student_admissionForm(request.POST)
        if form.is_valid():
            form.save()
            form = Student_admissionForm()
    context = {'form' : form}
    return render(request, 'create.html', context)

