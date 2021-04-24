from django.db import models
from .customer import Customer
from .product import Product

class Order(models.Model) :
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=150,null=True)
    discount = models.DecimalField(max_digits=9,decimal_places=2,default=0)
    delivery_charge = models.DecimalField(max_digits=9,decimal_places=2,default=0)
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        print(orderitems)
        total = sum([item.get_total for item in orderitems])
        print('total:',total)
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def final_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        totall = total - self.discount + self.delivery_charge
        return totall