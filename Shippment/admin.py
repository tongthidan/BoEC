from django.contrib import admin

# Register your models here.
from Shippment.models import Shippment, GlobalShippment, InternalShippment

admin.site.register(Shippment)
admin.site.register(GlobalShippment)
admin.site.register(InternalShippment)