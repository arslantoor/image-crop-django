# Generated by Django 3.1 on 2021-01-25 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210125_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 19, 3, 56, 92773, tzinfo=utc)),
        ),
    ]
