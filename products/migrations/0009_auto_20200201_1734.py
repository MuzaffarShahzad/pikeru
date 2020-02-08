# Generated by Django 3.0.2 on 2020-02-01 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200201_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='shop/product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 1, 17, 34, 19, 190923)),
        ),
        migrations.AlterField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 1, 17, 34, 19, 191791)),
        ),
    ]
