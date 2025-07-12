from django.db import models



# Create your models here.


# Create your models here.
class Member(models.Model):
  id = models.IntegerField(primary_key=True)
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  phone = models.IntegerField(null=True)
  join_date = models.DateField(null=True)

  def __str__(self):
    return self.Firstname