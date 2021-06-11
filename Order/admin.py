from django.contrib import admin

# Register your models here.
from Order.models import Item, Cart, Payment, CardATM, Wallet, Cash,Shippment, GlobalShippment, InternalShippment
    # Order

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(CardATM)
admin.site.register(Wallet)
admin.site.register(Cash)
admin.site.register(Shippment)
admin.site.register(GlobalShippment)
admin.site.register(InternalShippment)
# admin.site.register(Order)


