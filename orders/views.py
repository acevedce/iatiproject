from django.conf import settings
from django.core.mail import send_mail
from shop.models import Product
from django.http.response import HttpResponseRedirect
from datetime import date
from orders.models import OrderItem, Order, Transaction

import datetime
import random
import string
from django.http import JsonResponse
import json

session_id = settings.CART_SESSION_ID

def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str

def get_user_pending_order(request):
    # get order for the correct user
    order = Order.objects.filter(owner=session_id, is_ordered=False)
    order_details = {}
    if order.exists():
        # get the only order in the list of filtered orders
        order_details["products"] = order[0].get_cart_items()
        order_details["total_price"] = order[0].get_cart_total()
        return order_details
    return order_details

def manage_cart(request, **kwargs):
    if request.method == "POST":
        product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        quantity = 1
        if 'quantity' in body.keys():
            quantity = body['quantity']
        
        if quantity <= 0:
            #I PREFER USING METHOD DELETE
            return delete_from_cart(request, product, quantity)
        else:
            return add_to_cart(request, product, quantity)

def add_to_cart(request, product, quantity):
    update_item = OrderItem.objects.filter(product_id=product.pk)
    if update_item.exists():
        quantity += update_item[0].quantity
        status = OrderItem.objects.filter(product_id=product.pk).update(quantity=quantity)
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product, quantity=quantity)

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=session_id, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
 
    return JsonResponse(get_user_pending_order(request))

def delete_all_cart():
    OrderItem.objects.all().delete()

def delete_from_cart(request, product, quantity):
    item_id = product.pk
    new_quantity = 0
           
    item_to_delete = OrderItem.objects.filter(product_id=item_id)
    if item_to_delete.exists():
        if quantity == 0:
            item_to_delete[0].delete()
        elif quantity < 0:
            new_quantity = item_to_delete[0].quantity + quantity
            if new_quantity <= 0:
                item_to_delete[0].delete()
            else:            
                status = OrderItem.objects.filter(product_id=item_id).update(quantity=new_quantity)            
                order_item, status = OrderItem.objects.get_or_create(product=product, quantity=new_quantity)
                user_order, status = Order.objects.get_or_create(owner=session_id, is_ordered=False)
                user_order.items.add(order_item)
                if status:
                    # generate a reference code
                    user_order.ref_code = generate_order_id()
                    user_order.save()
    return JsonResponse(get_user_pending_order(request))


def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }

    return JsonResponse(existing_order)
    

def update_stock(request, order_items):
    for items in order_items:
        prods = Product.objects.filter(pk=items.product_id)
        item_to_update = prods[0]
        if items.product.current_stock >= items.quantity:
            new_stock = item_to_update.current_stock - items.quantity
            prods.update(current_stock=new_stock, updated=datetime.datetime.now())
            if new_stock == 0:
                prods.update(available=0, updated=datetime.datetime.now())
        else:
            delete_from_cart(request, item_to_update, 0)
            return 404
    return 201



def checkout(request, **kwargs):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # get the order being processed
        order_to_purchase = Order.objects.filter(owner=session_id, is_ordered=False)
        if order_to_purchase.exists():
            order_to_purchase = order_to_purchase[0]
            # update the placed order
            order_to_purchase.is_ordered=True
            order_to_purchase.date_ordered=datetime.datetime.now()
            order_to_purchase.save()
            
            order_items = order_to_purchase.items.all()
            order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())
            stock_status = update_stock(request, order_items)
            if stock_status != 201:
                return JsonResponse({"shipped":"One of the products is out of stock and has been removed from cart"})
            # create a transaction
            transaction = Transaction(profile=session_id,
                                    first_name = body['first_name'], 
                                    last_name = body['last_name'],
                                    address= body['address'],
                                    postal = body['postal'],
                                    email = body['email'],
                                    phone = body['phone'],
                                    order_id=order_to_purchase.id,
                                    amount=order_to_purchase.get_cart_total(),
                                    success=True)
            transaction.save()


            # send an email to the customer
            subject = 'hello {}'.format(request.POST.get('first_name', 'Joe'))
            message = 'Your order nr. {} has been shipped'.format(order_to_purchase.id)
            mail = send_mail(subject, message, 'admin@iati.com', [request.POST.get('email', 'none@none.com')])    
            # look at tutorial on how to send emails with sendgrid
            delete_all_cart()
            return JsonResponse({"shipped":True})
    return JsonResponse({"shipped":False})
