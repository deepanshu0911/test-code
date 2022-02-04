# Generated by Django 4.0 on 2022-01-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0004_client_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='openingBalance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='returnDues',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='salesDues',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
