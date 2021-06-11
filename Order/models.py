from django.db import models

# Create your models here.
import Order
from Product.models import Product


class Item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    # name = product.name;
    priceSale =models.DecimalField(max_digits=12, decimal_places=2)
    saleOff = models.FloatField()
    numberItem = models.IntegerField()

class Cart(models.Model):

    items = models.ForeignKey(Item, on_delete= models.CASCADE)
    statusCart = models.CharField(max_length=255)

class Payment(models.Model):
    ammount = models.FloatField()
class CardATM(Payment):
    card_id = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
class Wallet(Payment):
    producerWallet = models.CharField(max_length=100)

class Cash(Payment):
    CodePayment = models.CharField(max_length=100)

class Shippment(models.Model):
    dateShip = models.DateTimeField(max_length=100)
    dateReceive = models.DateTimeField(max_length=100)
    costShippment = models.FloatField()
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)

class InternalShippment(Shippment):
    distance = models.BigIntegerField()
    cityReceive = models.CharField(max_length=255)

class GlobalShippment(Shippment):
    countryReceive = models.CharField(max_length=255)




class Order(models.Model):
    STATUS = (
        ('True', 'Payment'),
        ('False', 'Not payment'),
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    dateOrder = models.DateTimeField()
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    shippment = models.OneToOneField(Shippment, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices= STATUS)

