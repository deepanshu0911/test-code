# Generated by Django 4.0 on 2022-01-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0019_quotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='salesDues',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
