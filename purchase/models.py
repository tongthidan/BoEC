import datetime
from pydoc import html

from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from Item.models import Item
from User.models import User, Customer, StaffSale


class Shippment(models.Model):
    TYPESHIP = (
        ('True','Internal Ship'),
        ('False','Global Ship')
    )
    STATUSSHIP = (
        ('1','Chưa giao'),
        ('2','Đang giao')
    )
    dateShip = models.DateTimeField(auto_now=True)
    timeDelivery = models.CharField(max_length=100)
    costShippment = models.FloatField()
    typeShippment = models.CharField(max_length=100,choices= TYPESHIP)
    statusShipping = models.CharField(max_length= 100, choices= STATUSSHIP)

    def __str__(self):
        if self.typeShippment == 'True':
            return mark_safe(html.escape(str('Internal Ship')))
        if self.typeShippment == 'False':
            return mark_safe(html.escape(str('Global Ship')))

class InternalShippment(Shippment):

    cityReceive = models.CharField(max_length=255)
class GlobalShippment(Shippment):
    countryReceive = models.CharField(max_length=255)

class Payment(models.Model):

    TYPEPAYMENT =(
        ('1','ATM Card'),
        ('2', 'Wallet'),
        ('3', 'Cash')
    )
    typePayment = models.CharField(max_length=100, choices=TYPEPAYMENT)
    ammount = models.FloatField()
    def __str__(self):
        if self.typePayment == '1':
            return mark_safe(html.escape(str('ATM Card')))
        if self.typePayment == '2':
            return mark_safe(html.escape(str('Wallet')))
        if self.typePayment == '3':
            return mark_safe(html.escape(str('Cash')))
class CardATM(Payment):
    card_id = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
class Wallet(Payment):
    producerWallet = models.CharField(max_length=100)
class Cash(Payment):
    CodePayment = models.CharField(max_length=100)

class Cart(models.Model):
    STATUS = (
        ('True', 'active'),
        ('False', 'inactive'),
    )
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    statusCart = models.CharField(max_length=100, choices= STATUS)
    total = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    def __str__(self):
        return  str(self.id)
class Order(models.Model):
    STATUSOrder = (
        ('True', 'Đã xử lý'),
        ('False', 'Chưa xử lý'),
    )
    staff = models.CharField(max_length=255)
    Customer = models.CharField(max_length= 100)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    shippment = models.ForeignKey(Shippment, on_delete=models.CASCADE)
    dateOrder = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUSOrder)

class Cart_Item(models.Model):
        STATUSOrder = (
        ('True', 'active'),
        ('False', 'inactive'),
        )
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        items = models.ForeignKey(Item, on_delete=models.CASCADE)
        numberItem = models.IntegerField()
        status=models.BooleanField(choices=STATUSOrder)

