from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="")
    Stock = models.IntegerField()
    price_dis = models.FloatField()
    percent_dis = models.FloatField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
