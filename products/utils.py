import json
from .models import *

def cookieCart(request) :
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('CART:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0,'final_total':0,'discount':0,'delivery_charge':0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:

            product = Product.objects.get(id=i)

            if product:
                cartItems += cart[i]['quantity']
                total = (product.product_price * cart[i]['quantity'])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'product': {
                        'id': product.id,
                        'product_name': product.product_name,
                        'product_des': product.product_des,
                        'product_price': product.product_price,
                        'imageURL': product.imageURL,
                    },
                    'quantity': cart[i]['quantity'],
                    'get_total': total,

                }

                items.append(item)

        except:
            pass
    order['final_total'] = order['get_cart_total'] + order['delivery_charge'] - order['discount']
    return {'items': items, 'order': order, 'cartItems':cartItems}

def cartData(request) :
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'items': items, 'order': order, 'cartItems': cartItems}


def guestOrder(request,data) :
    print('User not Authenticate')
    print('Cookies:', request.COOKIES)
    fname = data['form']['fname']
    lname = data['form']['lname']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.fname = fname
    customer.lname = lname

    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,

    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
    return customer,order