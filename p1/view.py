from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world')

def home(request):
    return render(request, 'sample1.html')

def second(request):
    return render(request, 'directry/sample2.html')

def third(request):
    return render(request, 'directry/third.html', {'data':'True statement block', 'name':'Fairoz khan'})

def fourth(request):
    fruits = ['Banana', 'Mango', 'Water melone', 'Musk melone', 'Orange']
    return render(request, 'directry/fourth.html', {'fruits':fruits})

def fifth(request):
    return  render(request, 'directry/fifth.html', {'a':10, 'b':5})
