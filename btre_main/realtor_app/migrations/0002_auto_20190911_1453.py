# Generated by Django 2.2.1 on 2019-09-11 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 9, 11, 14, 53, 6, 448712)),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
