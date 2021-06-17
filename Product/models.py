from django.db import models

# Create your models here.

# class Category(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.TextField(max_length=300)
from django.utils.safestring import mark_safe


class ProductSize( models.Model):
    size = models.CharField(max_length=50)
    descriptionSize = models.TextField(max_length=300)
    def __str__(self):
        return  self.size
class ProductColor(models.Model):
    color = models.CharField(max_length=50)
    colorCode = models.TextField(max_length=300)

    def __str__(self):
        return self.color

class ProductImage(models.Model):

    image = models.ImageField()



class Product( models.Model):
    name = models.CharField(max_length=255)
    priceInput = models.DecimalField(max_digits=12, decimal_places=2)
    picture=models.ImageField(blank=True, upload_to='images/')
    numberProduct = models.IntegerField(default=0)
    imageP = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format('/static' + self.image.url))
        else:
            return ""
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



