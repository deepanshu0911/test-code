# Generated by Django 4.0 on 2022-01-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0011_alter_invoice_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='whatsapp_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
