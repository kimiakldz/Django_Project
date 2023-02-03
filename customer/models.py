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


class Address(models.Model):
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    num = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=10)
