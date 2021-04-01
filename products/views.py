from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_grid(request):
    return render(request, 'products/product.html')

