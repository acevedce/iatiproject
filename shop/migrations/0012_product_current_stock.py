# Generated by Django 4.1.7 on 2023-03-08 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_stock',
            field=models.PositiveIntegerField(default=0, verbose_name='current stock'),
        ),
    ]