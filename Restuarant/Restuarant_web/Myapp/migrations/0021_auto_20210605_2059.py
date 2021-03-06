# Generated by Django 3.2.3 on 2021-06-05 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0020_alter_customer_entrydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentstock',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 5, 20, 59, 59, 463663)),
        ),
        migrations.AlterField(
            model_name='customerorderbooking',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customerorderdetail',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customerorderpayment',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='distributerbranddetail',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='distributercontactdetail',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='distributerpayment',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='distributerpersonaldetail',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employeecontactdetail',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employeepesonaldetail',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employeeprevoiusexperiance',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employeeskill',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='extras',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='foodingredient',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='foodsize',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='logindetail',
            name='LoginTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='CreateTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='offersfood',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productpurchase',
            name='PurchaseDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='EntryDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
