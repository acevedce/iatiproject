# Generated by Django 4.1.7 on 2023-03-06 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_color_brand_color_remove_color_primary_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='brand_color',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='primary_color',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='secondary_color',
        ),
        migrations.AddField(
            model_name='color',
            name='brand_color',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='brand color'),
        ),
        migrations.AddField(
            model_name='color',
            name='primary_color',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='primary color'),
        ),
        migrations.AddField(
            model_name='color',
            name='secondary_color',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='secondary color'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='colors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.color', verbose_name='product_colors'),
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='brands',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='sizes',
        ),
        migrations.AddField(
            model_name='productattribute',
            name='brands',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='shop.brand'),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='sizes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='shop.size'),
        ),
    ]
