"""TieuLuanKTPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name = 'home'),
    path('productDetail/<int:item_id>', views.ProductDetail, name = 'productDetail'),
    path('payment/',views.payment, name = 'order'),
    path('cart/',views.Cart, name = 'cart'),
    path('login/',views.Login,name = 'login'),
    path('register/',views.Register,name = 'register'),
    path('add-to-cart/',views.AddToCart ,name="add_to_cart"),
    path('confirm/' ,views.Confirm, name = 'confirm')
]
