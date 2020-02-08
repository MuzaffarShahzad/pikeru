# Generated by Django 3.0.2 on 2020-02-05 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200204_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 5, 17, 52, 33, 839775)),
        ),
        migrations.AlterField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 17, 52, 33, 840786)),
        ),
        migrations.AlterField(
            model_name='usernotes',
            name='notes_priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=10),
        ),
    ]
