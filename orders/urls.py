from django.urls import re_path

from .views import (
    manage_cart,
    order_details,
    checkout
)

app_name = 'orders'

urlpatterns = [
    re_path(r'^cart/(?P<item_id>[-\w]+)/$', manage_cart, name="manage_cart"),
    re_path(r'^cart/$', order_details, name="order_summary"),
    re_path(r'^checkout/$', checkout, name='checkout')
]