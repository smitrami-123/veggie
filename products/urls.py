from django.contrib import admin
from django.urls import path
from .views import product

app_name = 'products'

urlpatterns = [
    # /product/
    path('', product, name='product'),
]
