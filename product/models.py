import decimal

from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

class Size(models.Model):
    XSMALL = 'XS'
    SMALL = 'S '
    MEDIUM = 'M '
    LARGE = 'L '
    XLARGE = 'XL'

    Size_Choices = [
        (XSMALL, 'Xsmall'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XLARGE, 'Xlarge'),
    ]
    size = models.CharField(
        max_length=2,
        choices=Size_Choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.size


class Color(models.Model):
    BLACK = 'BK'
    WHITE = 'WT'
    RED = 'RD'
    BLUE = 'BU'
    GREEN = 'GR'

    Color_Choices = [
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
    ]
    color = models.CharField(
        max_length=2,
        choices=Color_Choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.get_color_display()


class Category(models.Model):
    """
            Stores product categories.
            Each category may have one parent and many children with self relation.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    image = models.ImageField(upload_to="product/", null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('landing:category_filter', args=[self.slug, ])


class Discount(models.Model):
    """
            Stores discount of products.
            Each discount may be set for several products.
    """
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.CharField(max_length=10, choices=(('P', 'Percent'), ('M', 'Money')), default='M')
    max = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.type}: {self.value}"


class Product(models.Model):
    """
            Stores details of products.
            Fields are based on our online clothes shop.
    """

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product/%Y/%m/", null=True, blank=True)
    Stock = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ManyToManyField(Category, related_name='products')
    discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sizes = models.ManyToManyField(Size, null=True, blank=True)
    colors = models.ManyToManyField(Color, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('landing:product_detail', args=[self.slug, ])

    def get_price(self):
        price = self.price
        if self.discount:
            if self.discount.type == 'M':
                price = price - self.discount.value
            else:
                price = price * decimal.Decimal(1 - (self.discount.value / 100))
        return round(price, 2)
