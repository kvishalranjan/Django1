# Generated by Django 3.2.4 on 2021-07-24 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_auto_20210724_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='expirydate',
            field=models.DateField(default=datetime.datetime(2021, 7, 24, 19, 43, 50, 253170)),
        ),
    ]
