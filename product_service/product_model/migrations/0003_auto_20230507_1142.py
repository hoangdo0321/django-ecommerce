# Generated by Django 3.2.18 on 2023-05-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_model', '0002_book_clothes_product_shoese'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shoese',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
