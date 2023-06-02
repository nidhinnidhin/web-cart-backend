from rest_framework import serializers
from django.http import Http404

from products.serializers import ProductListCreateSerializer
from . models import Wishlist

class wishlistSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request')

        if Wishlist.objects.filter(buyer = request.user, product = validated_data["product"]).exists():
            wishlist = Wishlist.objects.get(buyer = request.user, product = validated_data["product"])

            wishlist.save()

        return wishlist

    class Meta:
        product = ProductListCreateSerializer (read_only=True, many=True)
        model = Wishlist
        fields = ["product","id"]
        depth = 1

class WishlistListingSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request')
        wishlist = Wishlist()
        wishlist.buyer = request.user
        wishlist.product = validated_data["product"]
        wishlist.save()
        return wishlist

    class Meta:
        product = ProductListCreateSerializer (read_only=True, many=True)
        model = Wishlist
        fields = ["product"]    

class WishlistDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        exclude = ["buyer"]
    