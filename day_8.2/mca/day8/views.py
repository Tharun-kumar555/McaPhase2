from django.shortcuts import render
from django .http import HttpResponse
from .forms import StudentForm



# Create your views here.

def insert_student(request):
    context={}
    ob_form= StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Congratulations..!,Data will be saved succcesfully")
    context['form']=ob_form
    return render(request,"insert_student.html",context)
