from django.db import models

# Create your models here.

class Product(models.Model):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)

