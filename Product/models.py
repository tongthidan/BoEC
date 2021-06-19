from django.db import models

from django.utils.safestring import mark_safe
class Product( models.Model):
    TYPE = (
        ('1', 'Book'),
        ('2', 'Clothes'),
        ('3', 'Electronic')
    )
    typeProduct = models.CharField(max_length=10, choices= TYPE)
    nameProduct = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(max_length= 255)
    priceInput = models.DecimalField(max_digits=12, decimal_places=2)
    numberProduct = models.IntegerField(default=0)
    def __str__(self):
        return self.nameProduct

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format('/static' + self.image.url))
        else:
            return ""
class Book(Product):
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
class Electro(Product):

    producer = models.CharField(max_length=255)
    national = models.CharField(max_length=255)
class Clothes(Product):
    typeClothes = models.CharField(max_length=255)
    manufacture = models.CharField(max_length=255)
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    image = models.ImageField()
class ProductSize( models.Model):
    clothes = models.ForeignKey(Clothes, on_delete= models.CASCADE)
    size = models.CharField(max_length=50)
    descriptionSize = models.TextField(max_length=300)
    def __str__(self):
        return  self.size
class ProductColor(models.Model):
    color = models.CharField(max_length=50)
    colorCode = models.TextField(max_length=300)
    eletric = models.ForeignKey(Electro, on_delete= models.CASCADE)
    clothes =  models.ForeignKey(Clothes, on_delete= models.CASCADE)
    def __str__(self):
        return self.color







