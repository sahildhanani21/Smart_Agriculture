from django.db import models

# Create your models here.
class adminlogin(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class admindata(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)

class complaint(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    number = models.BigIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)