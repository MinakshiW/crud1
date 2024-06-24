from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=34)
    email = models.EmailField()
    mob = models.BigIntegerField()
    city = models.CharField(max_length=23)
    pincode = models.IntegerField()