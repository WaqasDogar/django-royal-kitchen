# Generated by Django 3.2.3 on 2021-06-04 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0013_auto_20210604_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 18, 46, 20, 860261)),
        ),
        migrations.AlterField(
            model_name='food',
            name='FoodImage',
            field=models.ImageField(upload_to='images'),
        ),
    ]
