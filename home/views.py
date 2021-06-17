from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request

from Item.models import Item
from Product.models import Product


def Home(request):
    products = Item.objects.all()
    context={
        'products':products
    }
    return render(request, 'index.html',context)
def ProductDetail(request,item_id):
    item= Item.objects.filter(id=item_id)
    context={
        'product':item
    }
    return  render(request,'productDetail.html',context)
def Payment(request):
    return render(request, 'payment.html')
def Cart(request):
    return render(request,'cart.html')
def Login(request):
    return  render(request,'login.html')
def Shop(request):
    return render(request,'shop.html')
def Register(request):
    return  render(request,'register.html')