from django.forms import fields
from . models import StudentModel
from django import forms

class StudentForm(forms.ModelForm):
    class  Meta:
        model=StudentModel
        fields='__all__'
        