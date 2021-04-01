from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to='products/', default='alter.png')
    product_des = models.CharField(max_length=300, default='')
