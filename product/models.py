from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)


class Discount(models.Model):
    value = models.FloatField()
    type = models.FloatField()
    max = models.FloatField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="")
    Stock = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE)