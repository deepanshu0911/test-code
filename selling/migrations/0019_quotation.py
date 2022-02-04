# Generated by Django 4.0 on 2022-01-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0018_alter_item_profit_margin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('quotation_id', models.AutoField(primary_key=True, serialize=False)),
                ('quotation_no', models.CharField(blank=True, max_length=50, null=True)),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('client_name', models.CharField(blank=True, max_length=50, null=True)),
                ('walk_in_client_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gstin', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('supply', models.CharField(blank=True, max_length=50, null=True)),
                ('items', models.TextField(blank=True, null=True)),
                ('discount_type', models.CharField(blank=True, max_length=50, null=True)),
                ('discount_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('shipping_charges', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('tax_rate', models.CharField(blank=True, max_length=50, null=True)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('whatsapp_no', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(default='Paid', max_length=50)),
                ('bill_file', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
