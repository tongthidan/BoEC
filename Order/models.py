from django.db import models

# Create your models here.
import Order
from Payment.models import Payment
from  Shippment.models import Shippment
from Item.models import Item

class Cart(models.Model):

    items = models.ForeignKey(Item, on_delete= models.CASCADE)
    statusCart = models.CharField(max_length=255)

class Order(models.Model):
    STATUS = (
        ('True', 'Payment'),
        ('False', 'Not payment'),
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    dateOrder = models.DateTimeField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    shippment = models.ForeignKey(Shippment, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices= STATUS)

