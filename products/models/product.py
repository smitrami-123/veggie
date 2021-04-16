from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to='products/', default='alter.png')
    product_des = models.CharField(max_length=300, default='')
    product_ratings = models.FloatField(default=3.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    def __str__(self):
        return f'ID : ' +str(self.id) +' and name : ' + str(self.product_name)