import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210401_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_ratings',
            field=models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
