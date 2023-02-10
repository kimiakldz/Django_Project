from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Discount(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.TextChoices('DiscountType', 'Price Percent')
    max = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.type}: {self.value}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="static/image", null=True, blank=True)
    Stock = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.price}$"
