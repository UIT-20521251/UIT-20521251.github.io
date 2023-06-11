# Generated by Django 4.1.3 on 2022-12-19 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_notification_time_alter_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='goods',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 15, 9, 0, 311481)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('Đấu giá thành công', 'Đấu giá thành công'), ('Đăng bán thành công', 'Đăng bán thành công'), ('Bán thành công', 'Bán thành công'), ('Đấu giá không thành công', 'Đấu giá không thành công')], default='Đấu giá thành công', max_length=100),
        ),
    ]
