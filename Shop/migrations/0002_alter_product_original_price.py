# Generated by Django 4.0.5 on 2022-07-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.PositiveIntegerField(),
        ),
    ]
