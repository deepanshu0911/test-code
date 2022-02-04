# Generated by Django 4.0 on 2022-02-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0007_companyprofile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('help_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('solution', models.TextField(default='Waiting for solution.')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]