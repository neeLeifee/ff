from django.shortcuts import render
from django.http import HttpResponse
from .models import MyNewModel

def base(request):
    return render(request, 'base.html')

def testingDB(request):
    a = MyNewModel.objects.create(name='Test', number='228', x='Testing_X! ' * 100)
    return HttpResponse('<h1>Тестируем базу данных</h1> <br> <h1>Name:</h1>{} <h1>Number:</h1>{} <br> <h1>X:</h1>{}'.format(a.name, a.number, a.x))
