from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse("Hello,Django!")

def yes(request):
    return HttpResponse("<marquee><h1 >" 
    "I am Tharun Kumar"
    "</h1></marquee>")

def page(request):
         template = loader.get_template('new2.2.html')
         return HttpResponse(template.render())

# Create your views here.
