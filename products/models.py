from django.db import models


# Create your models here.
class Product(models.Model):
  title       = models.CharField(max_length=254)
  description = models.TextField()
  price = models.DecimalField(
    'price',
    decimal_places=3,
    max_digits=13,
    blank=True,
    null=True,
  )

