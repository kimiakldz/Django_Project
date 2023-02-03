from django.db import models


# Create your models here.
class Discount_code(models.Model):
    percent = models.FloatField()
    price = models.FloatField()
    max = models.FloatField()
    expire_date = models.DateField()
    one_time = models.BooleanField()
