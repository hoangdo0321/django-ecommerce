# Generated by Django 3.2.18 on 2023-05-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='productId',
            field=models.JSONField(max_length=10),
        ),
    ]