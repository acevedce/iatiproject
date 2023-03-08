from django.urls import re_path
from .views import (product_list, one_product)

app_name = 'shop'

urlpatterns = [
    re_path(r'^products/$', product_list, name='product-list'),
    re_path(r'^products/(?P<item_id>[-\w]+)/$', one_product, name="manage_product")
]