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
