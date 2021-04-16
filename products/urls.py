from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    # /product/
    path('', product, name='product'),

    # /product/num/
    path('<int:product_id>/', detail.as_view(), name='detail'),
]
