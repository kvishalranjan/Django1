from django.shortcuts import render
from .models import Person, Technology
from django.http import HttpResponse
from .forms import PersonForm
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to Home page of Accounts</h1>")

def person(request):
    try:
        data = request.GET['status']
        print(data)
        persons = Person.objects.filter(is_verify=data)
    except:
        persons = Person.objects.all()
        print("hai")
    context = {'persons':persons}
    return render(request, 'persons.html', context)


def technology(request):
    try:
        data = request.GET['technology_choice']
        print(data)
        if data == 'All':
           technology = Technology.objects.all()
        else: 
            carrers = Technology.objects.filter(carrer=data)
    except:
        carrers = Technology.objects.all()
    list1 = ['artificial_inteligence','data_scientist','blockchain','cloud_computing','cyber_security']
    context = {'technology':technology, 'list1': list1}
    return render(request, 'technology.html', context)

def create_person(request):
    form = PersonForm()
    context = {'form': form}
    return render(request, 'create.html', context)