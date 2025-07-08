from django.db import models

# Create your models here.
from django.db import models
class EmployeeModel(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10, unique=True)  
    email = models.EmailField()  
  
    def __str__(self):  
        return (self.first_name+' '+ self.last_name)
