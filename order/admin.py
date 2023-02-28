from django.contrib import admin
from .models import Order, OrderDetail, DiscountCode

# Register your models here.
admin.site.register(DiscountCode)


class OrderItemInLine(admin.TabularInline):
    model = OrderDetail
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'total_price', 'user')
    list_filter = ('user', 'discount_code')
    inlines = (OrderItemInLine, )
