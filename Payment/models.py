from django.db import models

# Create your models here.
class Payment(models.Model):
    ammount = models.FloatField()
class CardATM(Payment):
    card_id = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
class Wallet(Payment):
    producerWallet = models.CharField(max_length=100)

class Cash(Payment):
    CodePayment = models.CharField(max_length=100)
