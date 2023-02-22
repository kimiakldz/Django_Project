from django.db import models
from accounts.models import User, Address
from product.models import Product
from core import settings


# Create your models here.
class DiscountCode(models.Model):
    """Example of docstring on the __init__ method.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            """
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.TextChoices('DiscountType', 'Price Percent')
    max = models.DecimalField(max_digits=20, decimal_places=2)
    expire_date = models.DateField(null=True, blank=True)
    one_time = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type}: {self.value}"


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
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True,
                                related_name='orders')
    code_id = models.ForeignKey(DiscountCode, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True,)

    def get_subtotal_price(self):
        return sum(item.get_cost() for item in self.items.all())

    class Mete:
        ordering = ('-created')

    def __str__(self):
        return f"{self.user_id} - ${self.total_price}"


class OrderDetail(models.Model):
    """
        Stores details of all items in each order from shopping cart.
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order_id}: {self.id}"

    def get_cost(self):
        return self.price * self.quantity
