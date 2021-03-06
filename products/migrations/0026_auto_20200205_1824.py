# Generated by Django 3.0.2 on 2020-02-05 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20200205_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 5, 18, 24, 54, 426572)),
        ),
        migrations.AlterField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 18, 24, 54, 427631)),
        ),
        migrations.AlterField(
            model_name='usernotes',
            name='notes_priority',
            field=models.CharField(choices=[('Medium', 'Medium'), ('High', 'High'), ('Low', 'Low')], max_length=10),
        ),
    ]
