from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Wishlist(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.RESTRICT)
    product = models.ForeignKey(Product, on_delete = models.RESTRICT)

    def __str__(self):
        return f"{self.buyer.username} --> {self.product.name[:50]}"