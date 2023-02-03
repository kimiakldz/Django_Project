from django.db import models
from customer.models import Customer, Address


# Create your models here.
class Discount_code(models.Model):
    percent = models.FloatField()
    price = models.FloatField()
    max = models.FloatField()
    expire_date = models.DateField()
    one_time = models.BooleanField()


class Order(models.Model):
    total_price = models.FloatField()
    date = models.DateTimeField()
    status = models.TextChoices('OrderStatus', 'Ordered InProgress Sent Delivered')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount_code, on_delete=models.CASCADE)
