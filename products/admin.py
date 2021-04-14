from django.contrib import admin
from .models.product import *
# Register your models here.


class ProdGalleryAdmin(admin.StackedInline):
    model = ProdGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProdGalleryAdmin]

    class Meta:
        model = Product


@admin.register(ProdGallery)
class ProdGalleryAdmin(admin.ModelAdmin):
    pass

