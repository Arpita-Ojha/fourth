from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return HttpResponse('<h1>This is first view of app2</h1>')

def jimin(request):
    return render(request,'jimin.html')