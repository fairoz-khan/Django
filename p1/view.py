from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')

def home(request):
    return HttpResponse('<h1>Python is my favorite programming language</h1>')