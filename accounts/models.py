from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from core import settings
from iranian_cities.fields import OstanField, ShahrestanField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    """
        Stores users information, inherited from django AbstractUser
    """

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = None
    phone = models.CharField(max_length=11, null=True, blank=True)

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
    """
        Stores users addresses separately.
        In case that user may have several addresses.

        Using Iranian cities database to choose province and cities of Iran
        as a dropdown Menu.
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


# class OtpCode(models.Model):
#     """
#         Stores a six digit verification code for each email register confirmation.
#     """
#     email = models.EmailField()
#     code = models.PositiveSmallIntegerField()
#     created = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.code} to {self.email} at {self.created}"

# class Profile(models.Model):
#     """
#     Create a model named Profile for determinant if the e-mail is confirmed or not.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email_confirmed = models.BooleanField(default=False)
#
#
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     """
#     Add a Django signal. A new entry is added within the User model,
#     the signal is going to be trigger and add details in Profile model with default django email confirm as false.
#     """
#     if created:
#         Profile.objects.create(user=instance)
#         instance.profile.save()
