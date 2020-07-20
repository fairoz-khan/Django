from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello world')

def home(request):
    return render(request, 'sample1.html')

def second(request):
    return render(request, 'directry/sample2.html')
