from django.db import models
from django import forms


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, widget=forms.PasswordInput)


