from django.db import models
from shop.models import Product

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity =  models.PositiveIntegerField(default=0,verbose_name="items quantity")
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.CharField(max_length=15)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        items = self.items.all()
        data = []
        for i in items:
            det = {}
            det["id"] = i.product.id
            det["image_url"] = i.product.image_url
            det["description"] = i.product.description
            det["unit_price"] = i.product.price
            det["current_stock"] = i.product.current_stock
            det["quantity"] = i.quantity
            data.append(det)
        return data

    def get_cart_total(self):
        return sum([(item.product.price*item.quantity) for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class Transaction(models.Model):
    profile = models.CharField(max_length=15)
    first_name = models.CharField(max_length=120, verbose_name="first name", default="Joe") 
    last_name = models.CharField(max_length=120, verbose_name="last name", default="Doe")
    address= models.CharField(max_length=120, verbose_name="address", default="unknown")
    postal = models.CharField(max_length=120, verbose_name="postal code", default="0000")
    email = models.EmailField(default="unknown@hunknown.com", verbose_name="email")
    phone = models.CharField(max_length=34, default="000000-00000",verbose_name="phone")
    order_id = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=60, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']







        