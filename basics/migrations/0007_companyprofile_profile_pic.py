# Generated by Django 4.0 on 2022-01-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0006_alter_unit_unit_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='profile_pic',
            field=models.FileField(default='uploads/store_profile/FK.png', upload_to=''),
        ),
    ]