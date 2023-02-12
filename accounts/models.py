from django.db import models
from django import forms


# Create your models here.
class Customer(models.Model):
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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10, null=True, blank=True)
    username = models.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    """Example of docstring on the __init__ method.

            The __init__ method may be documented in either the class level
            docstring, or as a docstring on the __init__ method itself.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            Note:
                Do not include the `self` parameter in the ``Args`` section.
            """
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    num = models.CharField(max_length=5, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.province}/{self.city}"




