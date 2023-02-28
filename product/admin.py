from django.contrib import admin
from .models import Category, Product, Discount, Size, Color
# Register your models here.
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Size)
admin.site.register(Color)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ('category',)
	search_fields = ('category',)