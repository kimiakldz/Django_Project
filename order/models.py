from django.db import models
from accounts.models import Customer, Address
from product.models import Product


# Create your models here.
class DiscountCode(models.Model):
    value = models.FloatField()
    type = models.FloatField()
    max = models.FloatField()
    expire_date = models.DateField()
    one_time = models.BooleanField()


class Order(models.Model):
    total_price = models.FloatField()
    date = models.DateTimeField()
    status = models.TextChoices('OrderStatus', 'Ordered InProgress Sent Delivered')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    code_id = models.ForeignKey(DiscountCode, on_delete=models.CASCADE)


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
