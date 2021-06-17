from django.db import models

# Create your models here.
from Product.models import Product

class Item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    priceSale =models.DecimalField(max_digits=12, decimal_places=2)
    saleOff = models.FloatField()
    numberItem = models.IntegerField()
    def __str__(self):
        return  self.product.name
