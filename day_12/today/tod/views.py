from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('temp.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.

def displaygreen(request):
    stu=[{'name':'shiva','marks':90},{'name':'navmohan','marks':85},
         {'name':'shravani','marks':88},{'name':'salma','marks':91}]
    
    return render(request,'green.html',{'data': stu})


def display(request):
   stud=['shiva','navmohan','shravani','salma']
  
   return render(request,'greencol.html',{'data': stud})

