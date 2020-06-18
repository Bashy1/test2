from django.db import models
from django import forms
# Create your models here.


class Prospect(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    interest_area = models.TextField(max_length=200)

    def __str__(self):
        return(self.name)

