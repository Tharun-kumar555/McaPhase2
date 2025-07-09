from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def Home(request):
    return render (request,'Home.html')

def Ad(request):
    return render (request,'Admin.html')

def At(request):
    return render (request,'Attendence.html')

def Ac(request):
    return render (request,'Accounts.html')

def index(request):
    return render (request,'app1.html')

