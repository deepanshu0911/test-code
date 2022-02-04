# Generated by Django 4.0 on 2022-01-30 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_id', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gstin', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('purchase_no', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('supply', models.CharField(blank=True, max_length=50, null=True)),
                ('items', models.TextField(blank=True, null=True)),
                ('discount_type', models.CharField(blank=True, max_length=50, null=True)),
                ('discount_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('shipping_charges', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('tax_rate', models.CharField(blank=True, max_length=50, null=True)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('due_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('pay_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('pay_note', models.TextField(blank=True, null=True)),
                ('whatsapp_no', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(default='Paid', max_length=50)),
                ('bill_file', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
