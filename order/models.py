from django.db import models
from accounts.models import Customer, Address
from product.models import Product


# Create your models here.
class DiscountCode(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.TextChoices('DiscountType', 'Price Percent')
    max = models.DecimalField(max_digits=20, decimal_places=2)
    expire_date = models.DateField(null=True, blank=True)
    one_time = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type}: {self.value}"


class Order(models.Model):
    ORDERED = 'OR'
    INPROGRESS = 'IP'
    SENT = 'SE'
    DELIVERED = 'DE'
    Order_Status = [
        (ORDERED, 'Ordered'),
        (INPROGRESS, 'InProgress'),
        (SENT, 'Sent'),
        (DELIVERED, 'Delivered'),
    ]
    status = models.CharField(
        max_length=2,
        choices=Order_Status,
        default=ORDERED,
    )
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    code_id = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.date}ـ{self.total_price}$"


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
