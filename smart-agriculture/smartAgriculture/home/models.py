from django.db import models
from django.db.models.base import Model

# Create your models here.
class user(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=250)

    def __str__(self):
        return self.email