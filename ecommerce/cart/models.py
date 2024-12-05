from django.db import models

from products.models import Product
from users.models import User

# Create your models here.
class Cart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = ('user', 'product')
