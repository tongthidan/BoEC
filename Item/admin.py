from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Item.models import Item
class display_item(admin.ModelAdmin):
    list_display = ['product','priceSale','saleOff','numberItem']
    search_fields = ['priceSale']
admin.site.register(Item,display_item)
