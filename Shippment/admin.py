from django.contrib import admin

# Register your models here.
from Shippment.models import Shippment, GlobalShippment, InternalShippment
class display_Shippment(admin.ModelAdmin):
    list_display = ['typeShippment','dateShip','dateReceive','costShippment']
    search_fields = ['costShippment']
class display_internalShip(admin.ModelAdmin):
    list_display = ['typeShippment', 'cityReceive','dateShip','dateReceive', 'costShippment']
    search_fields = ['cityReceive']
class display_globalShip(admin.ModelAdmin):
    list_display = [ 'typeShippment','countryReceive','dateShip','dateReceive', 'costShippment']
    search_fields = ['countryReceive']
admin.site.register(Shippment,display_Shippment)
admin.site.register(GlobalShippment,display_globalShip)
admin.site.register(InternalShippment,display_internalShip)