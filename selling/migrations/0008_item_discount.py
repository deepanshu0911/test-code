# Generated by Django 4.0 on 2022-01-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0007_invoice_item_tax_amount_item_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
