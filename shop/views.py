#!/usr/bin/python
# - *- coding: utf-8 - *-
from .models import Product, Category, Diversity, Size, Composition, Color, Brand
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def create_product(request):
    name = request.POST.get('name')
    slug = request.POST.get('slug')
    description= request.POST.get('description')
    price = request.POST.get('price')
    category = request.POST.get('category')
    image_url = request.POST.get('image_url')
    available = request.POST.get('available') 
    brands = Brand.objects.filter(pk=int(request.POST.get('brands')))[0]
    colors= Color.objects.filter(pk=int(request.POST.get('colors')))[0]
    stock = request.POST.get('stock')
    current_stock = request.POST.get('current_stock')
    image_url = request.POST.get('image_url')
    if int(category) == 2:
        category = Category.objects.filter(pk=int(category))[0]
        diversities = Diversity.objects.filter(pk=int(request.POST.get('diversities')))[0]
        sizes = Size.objects.filter(pk=int(request.POST.get('sizes')))[0]
        sleeves = request.POST.get('sleeves')
        compositions = Composition.objects.filter(pk=int(request.POST.get('compositions')))[0]
    else:
        category = Category.objects.filter(pk=int(category))[0]
        diversities = None
        sizes = None
        sleeves = None
        compositions = None

    product = Product(name = name, \
                    slug = slug,\
                    description = description,\
                    price = price,\
                    category = category,\
                    image_url = image_url,\
                    available = available, \
                    brands = brands,\
                    colors= colors,\
                    stock = stock,\
                    current_stock = current_stock,\
                    diversities = diversities,\
                    sizes = sizes,\
                    sleeves = sleeves,\
                    compositions = compositions)
    product.save()    
# list
def product_list(request, category_slug=None):
    if request.method == "POST":
        create_product(request)
    jsonproducts = []
    products = Product.objects.filter(available=True)
    jsonproducts = get_product_details(products)

    return JsonResponse({"products":jsonproducts})


def get_product_details(products):
    jsonproducts = []
    if len(products) > 0:
        for p in products:
            jsonproduct = {}
            jsonproduct["id"] = p.id
            jsonproduct["name"] = p.name
            jsonproduct["slug"] = p.slug
            jsonproduct["description"] = p.description
            jsonproduct["price"] = p.price
            jsonproduct["created"] = p.created
            jsonproduct["updated"] = p.updated
            jsonproduct["category"] = p.category.name
            jsonproduct["image_url"] = p.image_url
            jsonproduct["available"] = p.available
            jsonproduct["brand"] = p.brands.brand
            jsonproduct["colors"] = {"primary":p.colors.primary_color, "secondary":p.colors.secondary_color, "brand":p.colors.brand_color}
            jsonproduct["stock"] = p.stock
            jsonproduct["current_stock"] = p.current_stock

            if p.category.name == "shirt":
                jsonproduct["diversities"] = p.diversities.diversity
                jsonproduct["sizes"] = p.sizes.size_num
                jsonproduct["sleeves"] = p.sleeves
                jsonproduct["compositions"] = {"cotton": p.compositions.cotton,
                                                "linen": p.compositions.linen,
                                                "hemp": p.compositions.hemp,
                                                "polyester": p.compositions.polyester,
                                                "nylon": p.compositions.nylon,
                                                "wool": p.compositions.wool,
                                                "silk": p.compositions.silk
                                            }
            jsonproducts.append(jsonproduct)
    return jsonproducts

def one_product(request, item_id):
    product = None
    if request.method == "DELETE":
        items, product = Product.objects.filter(pk=int(item_id)).delete()
    if request.method == "GET":
        product = Product.objects.filter(pk=int(item_id))
        product = get_product_details(product)

    return JsonResponse({"products":product})