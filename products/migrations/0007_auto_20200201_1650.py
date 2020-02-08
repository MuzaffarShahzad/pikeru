# Generated by Django 3.0.2 on 2020-02-01 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200201_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='scale',
            field=models.CharField(choices=[('I', 'Items'), ('C', 'Carton'), ('P', 'Pack'), ('K', 'KG'), ('P', 'Pound'), ('M', 'Meter'), ('R', 'Room')], default='I', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='max_user',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 1, 16, 50, 14, 94973)),
        ),
        migrations.AlterField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 1, 16, 50, 14, 95897)),
        ),
    ]
