# Generated by Django 3.1.7 on 2021-04-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='alter.png', upload_to='uploads/products/'),
        ),
    ]