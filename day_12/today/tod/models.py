from django.db import models

# Create your models here.
class Member(models.Model):
  ID = models.IntegerField(int)
  firstname = models.CharField(max_length=25)
  lastname = models.CharField(max_length=25)
  Phone = models.IntegerField(int)
  Join_date = models.DateField( auto_now=False, auto_now_add=False)