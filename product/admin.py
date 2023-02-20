from django.contrib import admin
from .models import Category, Product, Discount
# Register your models here.
admin.site.register(Category)

admin.site.register(Discount)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ('category_id',)
	search_fields = ('category_id',)