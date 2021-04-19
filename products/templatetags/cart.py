from django import template

register = template.Library()




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

# @register.filter(name='global_total_quan')
# def global_total_quan(cart) :
#     products = cart.keys()
#     sum = 0
#     for p in products :
#         sum += 1
#     return sum


