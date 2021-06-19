from django.contrib import admin

# Register your models here.

from Product.models import Product, Book, ProductImage, ProductColor, ProductSize, Electro, Clothes

class display_product(admin.ModelAdmin):
    list_display = ['picture','nameProduct','priceInput','numberProduct']
    search_fields = ['nameProduct']
class display_productColor(admin.ModelAdmin):
    list_display = ['color','colorCode']
class display_productSize(admin.ModelAdmin):
    list_display = ['size','descriptionSize']
class display_productImage(admin.ModelAdmin):
    list_display = ['image','descriptionImage']
class display_productImage(admin.ModelAdmin):
    list_display = ['image']
    search_fields = ['name']
class display_Book(admin.ModelAdmin):
    list_display = ['nameProduct','author','publisher','description','numberProduct','priceInput']
    search_fields = ['nameProduct']
class display_Electro(admin.ModelAdmin):

        list_display = ['nameProduct', 'description','producer','national','priceInput', 'numberProduct']
        search_fields = ['nameProduct']

class display_Clothes(admin.ModelAdmin):
    search_fields = ['nameProduct']
    list_display = ['nameProduct', 'description','manufacture','priceInput', 'numberProduct']
admin.site.register(ProductImage)
admin.site.register(ProductColor, display_productColor)
admin.site.register(ProductSize, display_productSize)
admin.site.register(Product, display_product)
admin.site.register(Electro, display_Electro)
admin.site.register(Clothes, display_Clothes)
admin.site.register(Book, display_Book)