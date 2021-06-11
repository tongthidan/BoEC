from django.db import models

# Create your models here.
from Product.models import Product

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # name = product.name;
    priceSale =models.DecimalField(max_digits=12, decimal_places=2)
    saleOff = models.FloatField()
    numberItem = models.IntegerField()
