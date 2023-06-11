# Generated by Django 4.1.3 on 2022-12-10 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_goods_price_now_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 15, 31, 34, 397331)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('Đấu giá thành công', '1'), ('Đăng bán thành công', '2'), ('Bán thành công', '3'), ('Đấu giá không thành công', '4')], default='1', max_length=100),
        ),
    ]