# Generated by Django 4.1.3 on 2022-12-28 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_goods_status_alter_goods_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='status',
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 13, 13, 12, 738332)),
        ),
    ]