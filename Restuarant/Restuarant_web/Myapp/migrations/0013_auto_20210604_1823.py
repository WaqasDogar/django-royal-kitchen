# Generated by Django 3.2.3 on 2021-06-04 17:23

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0012_alter_customer_entrydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='FoodImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 18, 22, 11, 111281)),
        ),
        migrations.AlterField(
            model_name='food',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
