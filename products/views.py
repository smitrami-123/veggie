from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Product
from django.views import View
# Create your views here.


class cart(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids=ids)
        print(products)
        return render(request,'products/cart.html',{'products' : products})

    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        cancel = False
        cancel = request.POST.get('cancel')
        # print(cancel)
        if cart :
            quantity = cart.get(product)
            if quantity :
                if cancel :
                    # print("Yeah__Cancelled")
                    cart.pop(product)
        request.session['cart'] = cart
        print(cart)
        return redirect("products:cart")


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

class detail(View):
    def get(self, request, product_id) :
        cart = request.session.get('cart')
        if not cart :
            request.session['cart'] = {}
        product_obj = Product.objects.get(pk=product_id)
        # product_obj = list(obj)
        p_range = range(0, int(product_obj.product_ratings))
        # converted to int as the float can't be passed to range func
        context = {
            'product_obj': product_obj,
            'p_range': p_range,
            'p_text': product_obj.product_des,
        }
        #print("product_id :",product_id)
        return render(request, 'products/detail_page.html', context)

    def post(self,request,product_id):
        product= request.POST.get('product')
        remove = False
        remove = request.POST.get('remove')
        cart = request.session.get('cart')


        if cart :
            quantity = cart.get(product)
            if quantity:
                if remove :
                    if quantity<=1 :
                        cart.pop(product)
                    else :
                        cart[product] = quantity - 1

                else :
                    cart[product]= quantity + 1
            else :
                if not remove :
                    cart[product] = 1


        else :
            cart = {}
            cart[product] = 1
        #print(product,'product')

        request.session['cart'] = cart
        print( request.session.get('user_email'),":",request.session['cart'])

        return redirect('products:detail',product_id)




# def detail(request, product_id):
#     product_obj = Product.objects.get(pk=product_id)
#     # product_obj = list(obj)
#     p_range = range(0, int(product_obj.product_ratings))
#     # converted to int as the float can't be passed to range func
#     context = {
#         'product_obj': product_obj,
#         'p_range': p_range,
#         'p_text': product_obj.product_des,
#     }
#     return render(request, 'products/detail_page.html', context)
