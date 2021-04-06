from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
# Create your views here.


def product(request):
    all_products = Product.objects.all().order_by('pk')
    paginator = Paginator(all_products, 12)
    page_num = request.GET.get('page')
    page_products = paginator.get_page(page_num)
    num_pages = paginator.num_pages + 1
    page_range = range(1, num_pages)
    context = {
        'page_products': page_products,
        'num_pages': page_range,
    }
    return render(request, 'products/product.html', context)
