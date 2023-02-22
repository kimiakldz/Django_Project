from django.contrib import admin
from .models import Order, OrderDetail, DiscountCode

# Register your models here.
admin.site.register(DiscountCode)


class OrderItemInLine(admin.TabularInline):
    model = OrderDetail
    raw_id_fields = ('product_id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'total_price', 'user_id')
    list_filter = ('user_id', 'code_id')
    inlines = (OrderItemInLine, )
