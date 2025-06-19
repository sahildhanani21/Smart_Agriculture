from django.db import models

# Create your models here.

class userregistertable(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uspass = models.CharField(max_length=30)
    uscpass = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)

