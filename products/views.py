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


def detail(request, product_id):
    product_obj = Product.objects.get(pk=product_id)
    # product_obj = list(obj)
    p_range = range(0, int(product_obj.product_ratings))
    # converted to int as the float can't be passed to range func
    context = {
        'product_obj': product_obj,
        'p_range': p_range,
        'p_text': product_obj.product_des,
    }
    return render(request, 'products/detail_page.html', context)
