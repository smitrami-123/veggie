from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *
from .utils import *
import datetime
import json

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action=='add':
        orderItem.quantity += 1
    elif action=='remove':
        orderItem.quantity -= 1
    elif action=='cancel' :
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity<=0 :
         orderItem.delete()


    return JsonResponse('Item was added', safe=False)

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
    if request.user.is_authenticated:
        customer = request.user.customer
        product_obj = Product.objects.get(pk=product_id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product_obj)
        # p_range = range(0, int(product_obj.product_ratings))
        cartItems = order.get_cart_items
        context = {
            'product_obj': product_obj,
            'orderItem' : orderItem,
            # 'p_range': p_range,
            'cartItems': cartItems,

        }
        return render(request, 'products/detail_page.html', context)
    else :

        orderitems = {'quantity' : 0}
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}



        product_obj = Product.objects.get(pk=product_id)
        if product_obj:
            try :
                orderitems['quantity'] = cart[str(product_obj.id)]['quantity']
            except :
                orderitems['quantity'] = 0
            context = {
                    'product_obj': product_obj,
                    'orderItem': orderitems,
                    # 'p_range': p_range,
                    'cartItems': cartItems,

                }
            return render(request, 'products/detail_page.html', context)
        else :
            return redirect('/home/error.html')








def cart(request) :
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, 'products/cart.html', context)

def checkout(request) :
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request,'products/checkout.html',context)

def processOrder(request) :
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)



    else :
        print('User not Authenticate')
        print('Cookies:',request.COOKIES)
        fname = data['form']['fname']
        lname = data['form']['lname']
        email = data['form']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']

        customer,created = Customer.objects.get_or_create(
            email = email,
        )
        customer.name = fname


        customer.save()

        order = Order.objects.create(
            customer = customer,
            complete = False,

        )

        for item in items :
            product = Product.objects.get(id = item['product']['id'])
            orderItem = OrderItem.objects.create(
                product = product,
                order = order,
                quantity = item['quantity'],
            )

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.get_cart_items > 0:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address1=data['shipping']['address1'],
            address2=data['shipping']['address2'],
            nation=data['shipping']['nation'],
            state=data['shipping']['state'],
            city=data['shipping']['city'],
            zipcode=data['shipping']['code'],

        )

    print('Data:', request.body)
    return JsonResponse('Payment Complete',safe=False)