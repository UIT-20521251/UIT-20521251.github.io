# Generated by Django 4.1.3 on 2022-12-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_goods_price_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, default='Nam', max_length=10),
        ),
    ]