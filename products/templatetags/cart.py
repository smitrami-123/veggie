from django import template
from products.models import *
import json
register = template.Library()



@register.filter(name='identity')
def identity(email):
    if email :
        return True
    return False


@register.filter(name='is_in_cart')
def is_in_cart(product,cart) :
    keys = cart.keys()
    for id in keys :
        if product.id == int(id) :
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart) :
    keys = cart.keys()
    for id in keys :
        if product.id == int(id) :
            return cart.get(id)
    return False

@register.filter(name='price_total')
def price_total(product,cart) :
    return product.product_price * cart_quantity(product,cart)

@register.filter(name='cart_total')
def cart_total(products, cart) :
    sum = 0
    for p in products :
        sum += price_total(p,cart)
    return sum

@register.filter(name='cart_total_quan')
def cart_total_quan(products, cart) :
    sum = 0
    for p in products :
        sum += cart_quantity(p,cart)
    return sum

@register.filter(name='global_total_quan')
def global_total_quan(request) :

    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        return cartItems
    else :
        sum = 0
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}

        for i in cart:
            try:
                product = Product.objects.get(id=i)
                if product:
                    sum += cart[i]['quantity']
            except :
                pass
        return sum


