from django.db import models

from products.models import Product
from users.models import User

# Define order status choices
ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

# Create your models here.
class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')
    # total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # shipping_address = models.TextField()
    # products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
