from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from pathlib import Path
from django.contrib import messages
import os
# Create your views here.

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'static/model.pickle')


def home(request, status):
    if status == "True":
        status = 1
    else:
        status = 0
    #persons = Person.objects.all()
    persons = Person.objects.filter(is_verify=status)

    context = {'persons': persons}
    return render(request, 'persons.html', context)


def person_filter(request):
    try:
        data = request.GET['filter']
        # persons = Person.objects.filter(gender=data).order_by('-id')
        persons = Person.objects.filter(gender=data)
        if data == 'All':
            persons = Person.objects.all()

    except:
        data = "All"
        persons = Person.objects.all()

    context = {'persons': persons, 'filter': data}
    return render(request, 'persons.html', context)


def create_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Object Saved Successfully")
            form = PersonForm()
        else:
            messages.error(request, "Please Provide valid data")

    #context = {'form': form, 'messages': messages}
    return render(request, 'create.html', locals())
    


