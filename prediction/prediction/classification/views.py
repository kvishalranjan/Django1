from django.shortcuts import render
from django.http import HttpResponse
from .models import PredResults
import pickle
# Create your views here.

def classify(request):
    try:
        species = request.GET
        species1 = species['iris'] 
        print(species)
        data1 = species.copy()
        data1.pop('user')
        list3 = [float(data1['Species']) if i == 'Species' else int(data1[i]) for i in data1.keys()]
        
        pickle_in = open('model.pickle', 'rb')
        reg = pickle.load(pickle_in)
        result = reg.predict([list3])
        if result[0]==1.0:
            res = 'Iris-setosa'
        else:
            res = 'Iris-versicolor'

        PredResults.objects.create(username = species['user'],
        
        SepalLengthCm = int(species['sepal_length']),
        SepalWidthCm = int(species['sepal_width']),
        PetalLengthCm = int(species['petal_length']),
        PetalWidthCm = int(species['petal_width']),
        predicted = res)

        g1 = PredResults.objects.all()
        list1 = []
        for i in g1: 
            list1.append(i.username)
        list1 = list(set(list1))
        print(list1)
        
        context = {'user_name':species['user'],'list1': list1}

        return render(request, 'classification/history.html', context)
    except Exception as e:
        print(e)
    return render(request, 'classification/classifyhome.html')


def history(request):
    try:
        data = request.GET['user']
        print(data)
        if data=='All':
            g_table = PredResults.objects.all()
        else:
            g_table = PredResults.objects.filter(username=data)
    except:
        g_table = PredResults.objects.all()
    g1 = PredResults.objects.all()
    list1 = []
    for i in g1: 
        list1.append(i.username)
    list1 = list(set(list1))
    print(list1)
    context = {'gc_table': g_table,'list1': list1}
    return render(request, 'classification/history.html', context)