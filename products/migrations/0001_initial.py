# Generated by Django 3.1.7 on 2021-03-31 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField(default=0)),
                ('product_img', models.ImageField(upload_to='products/')),
                ('product_des', models.CharField(default='', max_length=300)),
            ],
        ),
    ]