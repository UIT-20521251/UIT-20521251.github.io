# Generated by Django 4.1.3 on 2022-12-28 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_notification_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='status',
            field=models.CharField(default='Đang giao dịch', max_length=100),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 28, 15, 52, 49, 780806)),
        ),
    ]
