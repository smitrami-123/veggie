from django import template
from products.models import *
from products.utils import cookieCart
import json
register = template.Library()


@register.filter(name='is_there')
def is_there(productId,request) :
    if request.user.is_authenticated:
        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if orderItem.quantity :
                return True

        return False
    else :
        product = Product.objects.get(id=productId)
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        try :
            quan = cart[str(product.id)]['quantity']
            if  quan > 0 :
                return True
            else :
                return False
        except :
            return  False







