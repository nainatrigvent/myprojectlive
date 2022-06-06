from django.db import models
from django.forms import CharField
from ast import keyword
from operator import mod


# Create your models here.
class Country(models.Model): 
    name=models.CharField(max_length=200)
    continent=models.CharField(max_length=200)
    area=models.IntegerField(max_length=200)

    def __str__(self):
        return self.name

class State(models.Model):
    countryid=models.ForeignKey(Country,on_delete=models.CASCADE)
    name=models.CharField(max_length=200) 
    popuplation=models.IntegerField(max_length=200)
