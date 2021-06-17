from django.db import models

# Create your models here.
class Shippment(models.Model):
    TYPESHIP = (
        ('True','Internal Ship'),
        ('False','Global Ship')
    )
    dateShip = models.DateTimeField(max_length=100)
    dateReceive = models.DateTimeField(max_length=100)
    costShippment = models.FloatField()
    typeShippment = models.CharField(max_length=100,choices= TYPESHIP)
class InternalShippment(Shippment):

    distance = models.BigIntegerField()
    cityReceive = models.CharField(max_length=255)
class GlobalShippment(Shippment):
    countryReceive = models.CharField(max_length=255)
