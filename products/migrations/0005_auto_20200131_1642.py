# Generated by Django 3.0.2 on 2020-01-31 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200131_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 1, 31, 16, 42, 39, 899648)),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 31, 16, 42, 39, 898770)),
        ),
    ]
