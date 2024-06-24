from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=34)
    email = models.EmailField()
    mob = models.BigIntegerField()
    dob = models.DateField()
    city = models.CharField(max_length=23)