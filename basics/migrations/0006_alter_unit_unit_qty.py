# Generated by Django 4.0 on 2022-01-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0005_companyprofile_created_alter_tax_tax_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='unit_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]