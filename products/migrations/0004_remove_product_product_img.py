# Generated by Django 3.1.7 on 2021-03-31 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_img',
        ),
    ]