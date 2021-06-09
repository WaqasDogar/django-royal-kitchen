# Generated by Django 3.2.3 on 2021-06-04 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0018_auto_20210604_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 20, 23, 16, 336675)),
        ),
        migrations.AlterField(
            model_name='food',
            name='FoodImage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]