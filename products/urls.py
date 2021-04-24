from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    # /product/
    path('', product, name='product'),

    # /product/num/
    path('<int:product_id>/', detail, name='detail'),

    # /product/cart/
    path('cart/', cart, name='cart'),

    # product/checkout/
    path('checkout/', checkout, name='checkout'),

    path('updateItem/', updateItem, name='updateItem'),
    path('processOrder/', processOrder, name='processOrder')
]
