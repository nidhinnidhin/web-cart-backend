from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, upload_to = '')
    secondimage = models.ImageField(null=True, upload_to = '')
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null = True)
    category = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


