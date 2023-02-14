from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from core import settings
from iranian_cities.fields import OstanField, ShahrestanField


# Create your models here.
class User(AbstractUser):
    """
        Stores users information, inherited from django AbstractUser
    """
    phone = models.CharField(max_length=11, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        Simplest possible answer: Yes, always
        """
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Address(models.Model):
    """Example of docstring on the __init__ method.

            The __init__ method may be documented in either the class level
            docstring, or as a docstring on the __init__ method itself.

            Either form is acceptable, but the two should not be mixed. Choose one
            convention to document the __init__ method and be consistent with it.

            Note:
                Do not include the `self` parameter in the ``Args`` section.
            """
    province = OstanField()
    city = ShahrestanField()
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    num = models.CharField(max_length=5, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.province}/{self.city}"
