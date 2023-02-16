from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Category(models.Model):
    """
            Stores product categories.
            Each category may have one parent and many children with self relation.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="product/", null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.name}"


class Discount(models.Model):
    """
            Stores discount of products.
            Each discount may be set for several products.
    """
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.TextChoices('DiscountType', 'Price Percent')
    max = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.type}: {self.value}"


class Product(models.Model):
    """
            Stores details of products.
            Fields are based on our online clothes shop.
    """
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
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product/%Y/%m/", null=True, blank=True)
    Stock = models.IntegerField(validators=[MinValueValidator(0)])
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    discount_id = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}: {self.price}$"

    # def get_absolute_url(self):
    #     return reverse('home:category_filter', args=[self.slug, ])
