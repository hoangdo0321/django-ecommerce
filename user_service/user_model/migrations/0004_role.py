# Generated by Django 3.2.18 on 2023-05-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0003_auto_20230507_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
