# Generated by Django 3.2.18 on 2023-05-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartmodel_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='productId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
