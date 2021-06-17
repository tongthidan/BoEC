from django.contrib import admin

# Register your models here.
from Order.models import Cart, Order, Cart_Item
class display_Cart(admin.ModelAdmin):
    list_display = ['cart']
admin.site.register(Cart)
admin.site.register(Cart_Item);

admin.site.register(Order)


