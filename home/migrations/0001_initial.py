# Generated by Django 3.1.7 on 2021-04-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_img', models.ImageField(upload_to='carousel/')),
                ('label', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
