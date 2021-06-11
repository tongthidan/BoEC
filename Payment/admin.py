from django.contrib import admin

# Register your models here.
from Payment.models import Payment, CardATM, Wallet, Cash

admin.site.register(Payment)
admin.site.register(CardATM)
admin.site.register(Wallet)
admin.site.register(Cash)