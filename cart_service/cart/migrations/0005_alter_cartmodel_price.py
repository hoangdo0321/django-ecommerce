# Generated by Django 3.2.18 on 2023-05-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20230507_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='price',
            field=models.FloatField(),
        ),
    ]