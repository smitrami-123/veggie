from django.db import models

# Create your models here.

class Carousel(models.Model):
    carousel_img = models.ImageField(upload_to='carousel/')
    label = models.CharField(max_length=50)
