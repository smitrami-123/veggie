from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def product(request):
    all_products = Product.objects.all
    context = {
        'all_products': all_products
    }
    return render(request, 'products/product.html', context)



