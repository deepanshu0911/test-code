# Generated by Django 4.0 on 2022-01-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='username',
            field=models.CharField(default='Not set', max_length=50),
        ),
    ]
