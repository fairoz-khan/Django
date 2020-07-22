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

def urls_data(request, name):
    return HttpResponse(f"<h1>Hello {name}</h1>")

def url_cal(request, ab):
    Ab = list(map(int, ab.split(" ")))
    return HttpResponse(f"<h1>Maximum num is: {max(Ab)}</h1>")

def ovel(request, s):
    ovels = 'aeiouAEIOU'
    o = 0
    cnsnt = 0
    for i in s:
        if i in ovels:
            o += 1
        else:
            cnsnt += 1
    return render(request, 'directry/ovelops.html', {'string':s, 'ov':o, 'cons':cnsnt})
