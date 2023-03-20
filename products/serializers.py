from rest_framework import serializers
from products.models import Product 

class ProductListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"