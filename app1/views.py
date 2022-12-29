from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return HttpResponse('<h1>This page contain information about BTS</h1>')

def two(request):
    return HttpResponse('<h1>This page contain information about RM</h1>')

def v(request):
    return render(request,'v.html')
