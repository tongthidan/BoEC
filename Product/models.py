from django.db import models

# Create your models here.

# class Category(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.TextField(max_length=300)
class ProductSize( models.Model):
    size = models.CharField(max_length=50)
    descriptionSize = models.TextField(max_length=300)
class ProductColor(models.Model):
    color = models.CharField(max_length=50)
    colorCode = models.TextField(max_length=300)

class ProductImage(models.Model):

    image = models.ImageField()

class Product( models.Model):
    name = models.CharField(max_length=255)
    priceInput = models.DecimalField(max_digits=12, decimal_places=2)
    numberProduct = models.IntegerField(default=0)
    imageP = models.ForeignKey(ProductImage, on_delete=models.CASCADE)

class Book(Product):
    # product=models.ForeignKey(Product,on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
class Electro(Product):
    sizeP = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    colorP = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    producer = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    national = models.CharField(max_length=255)
class Clothes(Product):
    typeClothes = models.CharField(max_length=255)
    sizeP = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    colorP = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    manufacture = models.CharField(max_length=255)



