from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    fullName = models.CharField(max_length = 100, null = True)
    addressLine1 = models.CharField(max_length = 200, null = True)
    addressLine2 = models.CharField(max_length = 200, null = True)
    city = models.CharField(max_length = 200, null = True)
    country = models.CharField(null = True, max_length = 100)
    pincode = models.CharField(null = True, max_length = 20)
    mobile = models.CharField(null = True, max_length = 15)

    def __str__(self):
        return self.owner.username
