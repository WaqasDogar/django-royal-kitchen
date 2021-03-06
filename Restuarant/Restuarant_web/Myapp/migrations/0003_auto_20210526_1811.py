# Generated by Django 3.2.3 on 2021-05-26 17:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrderBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalBill', models.DecimalField(decimal_places=2, max_digits=8)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=30)),
                ('ProductSize', models.CharField(max_length=10)),
                ('ProductQuantity', models.IntegerField()),
                ('SalePrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('EntryDate', models.DateTimeField()),
                ('CustomerOrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.customerorderbooking')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentMedium', models.CharField(max_length=50)),
                ('PaymentAmount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('EntryDate', models.DateTimeField()),
                ('CustomerOrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.customerorderbooking')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryAddress', models.CharField(max_length=100)),
                ('ExpectedTime', models.CharField(max_length=10)),
                ('EntryDate', models.DateTimeField()),
                ('CustomerOrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.customerorderbooking')),
            ],
        ),
        migrations.CreateModel(
            name='DistributerBrandDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.CharField(max_length=30, unique=True)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.CharField(blank=True, max_length=50, unique=True)),
                ('PhoneNo', models.CharField(max_length=13, unique=True)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DistributerContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('PhoneNo', models.CharField(max_length=13)),
                ('LandLineNo', models.CharField(blank=True, max_length=15)),
                ('Email', models.CharField(blank=True, max_length=50)),
                ('Others', models.CharField(blank=True, max_length=100)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DistributerPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaidAmount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('RemaningAmount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('PaymentMethod', models.CharField(max_length=50)),
                ('PaymentType', models.CharField(max_length=13)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DistributerPersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('FatherName', models.CharField(max_length=30)),
                ('CNIC', models.CharField(blank=True, max_length=13, unique=True)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=8)),
                ('MaritalStatus', models.CharField(max_length=10)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobName', models.CharField(max_length=30)),
                ('EmployeementYears', models.IntegerField()),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Bonus', models.DecimalField(decimal_places=2, max_digits=8)),
                ('DutyStartTime', models.TimeField(blank=True)),
                ('DutyEndTime', models.TimeField(blank=True)),
                ('JobDescription', models.CharField(max_length=100)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address1', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('PhoneNo1', models.CharField(max_length=13, unique=True)),
                ('LandLineNo', models.CharField(blank=True, max_length=15)),
                ('Email', models.CharField(blank=True, max_length=50)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePesonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(blank=True, max_length=30)),
                ('CNIC', models.CharField(blank=True, max_length=13, unique=True)),
                ('FatherName', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=8)),
                ('MaritalStatus', models.CharField(max_length=10)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePrevoiusExperiance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganizationName', models.CharField(max_length=50)),
                ('JobName', models.CharField(max_length=50)),
                ('JobDescription', models.CharField(blank=True, max_length=100)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Others', models.CharField(blank=True, max_length=100)),
                ('EntryDate', models.DateTimeField()),
                ('EmployeePID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SkillName', models.CharField(max_length=50)),
                ('OrganizationName', models.CharField(max_length=50)),
                ('CertificationNumber', models.CharField(blank=True, max_length=50)),
                ('LearnStartDate', models.DateField()),
                ('LearnEndDate', models.DateField()),
                ('Others', models.CharField(blank=True, max_length=100)),
                ('EntryDate', models.DateTimeField()),
                ('EmployeePID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail')),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExtrasName', models.CharField(max_length=30)),
                ('ExtrasType', models.CharField(max_length=10)),
                ('ExtrasQuantity', models.IntegerField(blank=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Description', models.CharField(max_length=250)),
                ('EntryDate', models.DateTimeField()),
                ('EmployeePID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodName', models.CharField(max_length=30, unique=True)),
                ('FoodType', models.CharField(max_length=50)),
                ('FoodDescription', models.CharField(blank=True, max_length=100)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Size', models.CharField(max_length=10)),
                ('EntryDate', models.DateTimeField()),
                ('FoodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.food')),
            ],
        ),
        migrations.CreateModel(
            name='FoodSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodSize', models.CharField(max_length=10)),
                ('FoodPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('EntryDate', models.DateTimeField()),
                ('FoodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.food')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IngredientName', models.CharField(max_length=30, unique=True)),
                ('IngredientPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Size', models.CharField(blank=True, max_length=10)),
                ('Description', models.CharField(blank=True, max_length=100)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30, unique=True)),
                ('Email', models.CharField(max_length=50)),
                ('EntryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('LoginTime', models.DateTimeField()),
                ('LoginID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OfferName', models.CharField(max_length=30, unique=True)),
                ('OfferPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Availability', models.CharField(blank=True, max_length=10)),
                ('CreateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OffersFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('EntryDate', models.DateTimeField()),
                ('FoodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.food')),
                ('FoodSizeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.foodsize')),
                ('OfferID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.offers')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PurchasePrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Quantity', models.IntegerField()),
                ('Size', models.CharField(blank=True, max_length=10)),
                ('PurchaseDate', models.DateTimeField()),
                ('BrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.distributerbranddetail')),
                ('IngredientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DegreeName', models.CharField(max_length=50)),
                ('InstituteName', models.CharField(max_length=50)),
                ('PassingYear', models.CharField(blank=True, max_length=10)),
                ('ObtainedMarks', models.IntegerField()),
                ('TotalMarks', models.IntegerField()),
                ('Grade', models.CharField(blank=True, max_length=2)),
                ('Other', models.CharField(blank=True, max_length=100)),
                ('EntryDate', models.DateTimeField()),
                ('EmployeePID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail')),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Name',
            new_name='FirstName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='CNIC',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AddField(
            model_name='customer',
            name='Email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='EntryDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 26, 18, 11, 30, 177302)),
        ),
        migrations.AddField(
            model_name='customer',
            name='LastName',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='customer',
            name='PhoneNo1',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='foodingredient',
            name='FoodSizeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.foodsize'),
        ),
        migrations.AddField(
            model_name='foodingredient',
            name='IngredientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.ingredient'),
        ),
        migrations.AddField(
            model_name='employeecontactdetail',
            name='EmployeePID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail'),
        ),
        migrations.AddField(
            model_name='employee',
            name='EmployeePID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail'),
        ),
        migrations.AddField(
            model_name='distributerpayment',
            name='DistributerPID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.distributerpersonaldetail'),
        ),
        migrations.AddField(
            model_name='distributerpayment',
            name='PurchaseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.productpurchase'),
        ),
        migrations.AddField(
            model_name='distributercontactdetail',
            name='DistributerPID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.distributerpersonaldetail'),
        ),
        migrations.AddField(
            model_name='distributerbranddetail',
            name='DistributerPID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.distributerpersonaldetail'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='EmployeePID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail'),
        ),
        migrations.AddField(
            model_name='customerorderbooking',
            name='CustomerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.customer'),
        ),
        migrations.AddField(
            model_name='customerorderbooking',
            name='EmployeePID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employeepesonaldetail'),
        ),
        migrations.AddField(
            model_name='currentstock',
            name='IngredientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.ingredient'),
        ),
    ]
