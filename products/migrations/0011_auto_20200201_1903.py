# Generated by Django 3.0.2 on 2020-02-01 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200201_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productbooked',
            old_name='book_product',
            new_name='items',
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 1, 19, 3, 4, 845436)),
        ),
        migrations.AlterField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 1, 19, 3, 4, 846344)),
        ),
    ]
