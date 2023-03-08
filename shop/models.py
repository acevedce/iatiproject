#!/usr/bin/python
# - *- coding: utf-8 - *-

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Category",on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="product name")
    image_url = models.URLField(max_length = 200, null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True, verbose_name="des")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    sizes = models.ForeignKey('Size', related_name="product_sizes", null= True, default = 1, on_delete=models.CASCADE)
    compositions = models.ForeignKey('Composition', related_name="product_composition", null= True, default = 1, on_delete=models.CASCADE)
    colors = models.ForeignKey('Color', verbose_name="product_colors", default = 1, on_delete=models.CASCADE)
    brands = models.ForeignKey('Brand', related_name="product_brand", default = 1, on_delete=models.CASCADE)
    sleeves = models.BooleanField(verbose_name="has sleeves", null=True, blank=True)
    diversities = models.ForeignKey('Diversity', related_name="product_diversity", null=True, on_delete=models.CASCADE)
    current_stock = models.PositiveIntegerField(default=0,verbose_name="current stock")
    stock = models.PositiveIntegerField(default=0,verbose_name="stock")
    available = models.BooleanField(default=True, verbose_name="available")

    class Meta:
        ordering = ['category','created']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name


class Diversity(models.Model):
    diversity = models.CharField(max_length=10)

class Size(models.Model):
    size_num = models.CharField(max_length=10)

class Brand(models.Model):
    brand = models.CharField(max_length=100, verbose_name="marca")

class Color(models.Model):
    primary_color = models.CharField(max_length=30, verbose_name="primary color", null=True, blank=True)
    secondary_color = models.CharField(max_length=30, verbose_name="secondary color", null=True, blank=True)
    brand_color = models.CharField(max_length=30, verbose_name="brand color", null=True, blank=True)
    
class Composition(models.Model):
    cotton = models.PositiveIntegerField(default=0,verbose_name="cotton percent")
    linen = models.PositiveIntegerField(default=0,verbose_name="linen percent")
    hemp = models.PositiveIntegerField(default=0,verbose_name="hemp percent")
    polyester = models.PositiveIntegerField(default=0,verbose_name="polyester percent")
    nylon = models.PositiveIntegerField(default=0,verbose_name="nylon percent")
    wool = models.PositiveIntegerField(default=0,verbose_name="wool percent")
    silk = models.PositiveIntegerField(default=0,verbose_name="silk percent")