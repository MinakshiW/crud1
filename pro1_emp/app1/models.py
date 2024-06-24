from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=34)
    email =models.EmailField()
    dob = models.DateField()
    city = models.CharField(max_length=23)
    salary = models.IntegerField()