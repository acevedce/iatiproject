# Generated by Django 4.1.7 on 2023-03-08 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_transaction_address_transaction_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='phone',
            field=models.CharField(default='000000-00000', max_length=34, verbose_name='phone'),
        ),
    ]
