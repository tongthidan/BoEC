import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request

from Item.models import Item
from Product.models import Product
from purchase.models import Cart_Item, Cart, Order, Payment, Shippment


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

# def Cart(request):
#     return render(request,'cart.html')
def Login(request):
    return  render(request,'login.html')
def Confirm(request):
    return  render(request, 'Confirm.html')
def Shop(request):
    return render(request,'shop.html')
def Register(request):
    return  render(request,'register.html')

def AddToCart(request):
    user = request.user
    carts = Cart.objects.filter(customer=user.id)
    if carts:
        cart = Cart.objects.get(customer=user.id)
    else:
        cart = Cart()
        cart.customer_id = user.id
        cart.save()
        order = Order()
        order.save()
    if request.method =='POST':
        product_id=request.POST.get('product')
        number=int(request.POST.get('number'))


        cartitems=Cart_Item.objects.filter(cart=cart.id,status=True,items=product_id)

        if cartitems:
            item = Cart_Item.objects.get(items=product_id)
            item.numberItem +=number
            item.save()
        else:
            item=Cart_Item()
            item.cart_id=cart.id
            item.status=True
            item.numberItem=number
            item.items_id=product_id
            item.save()
        itemsInCart = Cart_Item.objects.filter(cart = cart.id,status=True)
    if request.method=='GET':
        itemsInCart = Cart_Item.objects.filter(cart=cart.id, status=True)
    context = {
            'listItem': itemsInCart

    }
    return render(request, 'Cart.html',context)

def payment(request):
    user = request.user
    carts = Cart.objects.get(customer=user.id)
    cartItems = Cart_Item.objects.filter(cart_id = carts.id, status= True)
    payments=Payment.objects.all()
    shipments=Shippment.objects.all()
    if request.method=='POST':
        payment_id=request.POST.get('payment')
        shipment_id=request.POST.get('shipment')
        order= Order()
        date=datetime.timezone
        order.dateOrder=date
        order.payment_id=payment_id
        order.shippment_id=shipment_id
        order.cart_id=carts.id
        order.Customer=user.username
        order.save()
        for i in cartItems:
            i.order_id=order.id
            i.save()

        return  redirect('home')
    context={
        "cartItems":cartItems,
        'payments':payments,
        'shipments':shipments
    }
    return render(request, 'payment.html',context)
