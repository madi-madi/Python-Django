# Generated by Django 2.2.4 on 2019-08-17 08:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 17, 8, 35, 23, 49014, tzinfo=utc)),
        ),
    ]
