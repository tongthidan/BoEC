from django.contrib import admin

# Register your models here.
from purchase.models import Payment, Wallet, Cash, Shippment, GlobalShippment, InternalShippment, Cart, Cart_Item, Order
from purchase.models import CardATM

class display_Shippment(admin.ModelAdmin):
    list_display = ['typeShippment','dateShip','timeDelivery','costShippment']
    search_fields = ['costShippment']
class display_internalShip(admin.ModelAdmin):
    list_display = ['typeShippment', 'cityReceive','dateShip','timeDelivery', 'costShippment']
    search_fields = ['cityReceive']
class display_globalShip(admin.ModelAdmin):
    list_display = [ 'typeShippment','countryReceive','dateShip','timeDelivery', 'costShippment']
    search_fields = ['countryReceive']

class display_Payment(admin.ModelAdmin):

    list_display = ['id','typePayment','ammount']

class display_Cart(admin.ModelAdmin):
        list_display = ['id', 'statusCart']

class display_ItemInCart(admin.ModelAdmin):
        list_display = ['cart_id', 'items', 'numberItem']

class display_Order(admin.ModelAdmin):
        list_display = ['id', 'payment', 'shippment', 'dateOrder', 'status']


    # Ship
admin.site.register(Shippment,display_Shippment)
admin.site.register(GlobalShippment,display_globalShip)
admin.site.register(InternalShippment,display_internalShip)
# Payment
admin.site.register(Payment,display_Payment)
admin.site.register(CardATM)
admin.site.register(Wallet)
admin.site.register(Cash)
# Order
admin.site.register(Cart, display_Cart)
admin.site.register(Cart_Item, display_ItemInCart);

admin.site.register(Order, display_Order)