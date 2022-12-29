from django.shortcuts import render


# Create your views here.

def bts(request):
    return render(request,'bts.html')