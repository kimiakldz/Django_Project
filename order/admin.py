from django.contrib import admin
from .models import Order, OrderDetail, DiscountCode

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(DiscountCode)
