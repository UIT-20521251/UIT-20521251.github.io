# Generated by Django 4.1.3 on 2022-12-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_firstname_profile_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='namem',
            field=models.CharField(default='12', max_length=100),
        ),
        migrations.AlterField(
            model_name='goods',
            name='user',
            field=models.CharField(default=100, max_length=100),
        ),
    ]
