# Generated by Django 4.1.7 on 2023-03-06 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='marca')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(max_length=30, verbose_name='primary color')),
                ('secondary_color', models.CharField(max_length=30, verbose_name='secondary color')),
                ('brand_color', models.CharField(max_length=30, verbose_name='brand color')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['created'], 'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleeves', models.BooleanField(blank=True, null=True, verbose_name='has sleeves')),
                ('brands', models.ManyToManyField(blank=True, null=True, related_name='product_brand', to='shop.brand')),
                ('colors', models.ManyToManyField(blank=True, null=True, related_name='product_colors', to='shop.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attrs', to='shop.product')),
                ('sizes', models.ManyToManyField(blank=True, null=True, related_name='product_sizes', to='shop.size')),
            ],
        ),
    ]
