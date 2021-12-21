from django.db import models

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=300)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
