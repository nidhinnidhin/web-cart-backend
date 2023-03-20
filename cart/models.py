from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Cart(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.RESTRICT)
    product = models.ForeignKey(Product, on_delete = models.RESTRICT)
    count = models.IntegerField(default = 1)
    checked_out = models.BooleanField(default = False, null=True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)
    DELIVERY_STATUS = [
        ("processing", "Processing"),
        ("packed", "Packed"),
        ("out_for_delivery", "Out For Delivery"),
        ("delivered", "Delivered")
    ]

    delivery_status = models.CharField(max_length = 50, choices = DELIVERY_STATUS, default = "processing")
    

    def __str__(self):
        return f"{self.buyer.username} --> {self.product.name[:50]}"

