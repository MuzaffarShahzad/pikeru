# Generated by Django 3.0.2 on 2020-02-04 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200203_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='No Location', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 4, 21, 26, 41, 734429)),
        ),
        migrations.AlterField(
            model_name='productbooked',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 21, 26, 41, 735437)),
        ),
        migrations.AlterField(
            model_name='usernotes',
            name='notes_priority',
            field=models.CharField(choices=[('Low', 'Low'), ('High', 'High'), ('Medium', 'Medium')], max_length=10),
        ),
    ]
