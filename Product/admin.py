from django.contrib import admin

# Register your models here.

from Product.models import Product, Book, ProductImage, ProductColor, ProductSize, Electro, Clothes

class display_product(admin.ModelAdmin):
    list_display = ['name']
class display_productColor(admin.ModelAdmin):
    list_display = ['color','colorCode']
class display_productSize(admin.ModelAdmin):
    list_display = ['size','descriptionSize']
class display_productImage(admin.ModelAdmin):
    list_display = ['image','descriptionImage']
class display_productImage(admin.ModelAdmin):
    list_display = ['image']

class display_Book(admin.ModelAdmin):
    list_display = ['name','numberProduct','author','publisher']

class display_Electro(admin.ModelAdmin):

        list_display = ['name', 'numberProduct', 'colorP', 'producer','national']


class display_Clothes(admin.ModelAdmin):
    list_display = ['name', 'numberProduct', 'colorP', 'sizeP', 'manufacture']
admin.site.register(ProductImage)
admin.site.register(ProductColor, display_productColor)
admin.site.register(ProductSize, display_productSize)
admin.site.register(Product, display_product)
admin.site.register(Electro, display_Electro)
admin.site.register(Clothes, display_Clothes)
admin.site.register(Book, display_Book)