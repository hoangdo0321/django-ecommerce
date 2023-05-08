# Generated by Django 3.2.18 on 2023-04-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('productId', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=5)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
