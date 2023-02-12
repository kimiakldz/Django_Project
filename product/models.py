from django.db import models


# Create your models here.


class Category(models.Model):
    """Example of docstring on the __init__ method.

            The __init__ method may be documented in either the class level
            docstring, or as a docstring on the __init__ method itself.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1 (str): Description of `param1`.
                param2 (:obj:`int`, optional): Description of `param2`. Multiple
                    lines are supported.
                param3 (:obj:`list` of :obj:`str`): Description of `param3`.

            """
    name = models.CharField(max_length=50)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Discount(models.Model):
    """Example of docstring on the __init__ method.

            The __init__ method may be documented in either the class level
            docstring, or as a docstring on the __init__ method itself.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            Note:
                Do not include the `self` parameter in the ``Args`` section..

            """
    value = models.DecimalField(max_digits=20, decimal_places=2)
    type = models.TextChoices('DiscountType', 'Price Percent')
    max = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.type}: {self.value}"


class Product(models.Model):
    """Example of docstring on the __init__ method.

            The __init__ method may be documented in either the class level
            docstring, or as a docstring on the __init__ method itself.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            """
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="static/image", null=True, blank=True)
    Stock = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.price}$"
