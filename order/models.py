import decimal

from django.db import models
from accounts.models import User, Address
from product.models import Product
from core import settings
from decimal import Decimal


# Create your models here.
class DiscountCode(models.Model):
    """Example of docstring on the __init__ method.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            """
    code = models.CharField(max_length=10, unique=True, default='code')
    value = models.IntegerField()
    type = models.CharField(max_length=10, choices=(('P', 'Percent'), ('M', 'Money')), default='M')
    max = models.DecimalField(max_digits=20, decimal_places=2)
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)
    one_time = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type}: {self.code}"


class Order(models.Model):
    """
        Stores paid orders from our shopping cart.
    """
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
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True,
                             related_name='orders')
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.DO_NOTHING, default=None, null=True, blank=True, )

    def get_subtotal_price(self):
        subtotal = sum(item.get_cost() for item in self.items.all())
        return round(subtotal, 2)

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount_code:
            if self.discount_code.type == 'M':
                total = total - self.discount_code.value
            else:
                total = total * decimal.Decimal(1 - (self.discount_code.value / 100))
        return round(total, 2)

    class Mete:
        ordering = ('-created')

    def __str__(self):
        return f"{self.user_id} - ${self.total_price}"


class OrderDetail(models.Model):
    """
        Stores details of all items in each order from shopping cart.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order_id}: {self.id}"

    def get_cost(self):
        return self.price * self.quantity
