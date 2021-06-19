from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class FullName(models.Model):
    first_name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __int__(self):
        return self.first_name + ' ' + self.midle_name + ' ' + self.last_name


class Address(models.Model):
    homeNumber = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


    def address(self):
        return self.homeNumber + " " + self.street + " " + self.city


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.OneToOneField(FullName, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
class Customer (User):
    TYPE = (
        ('1','Khách lẻ'),
        ('2','Khách buôn')
    )
    typeCustomer = models.CharField(max_length=100, choices= TYPE)
class StaffSale(models.Model):
    SHIP = (
        ('1',' Ca 1'),
        ('2', ' Ca 2'),
        ('3', ' Ca 3')
    )
    workShip = models.CharField(max_length= 100, choices= SHIP)
    KPI = models.IntegerField()