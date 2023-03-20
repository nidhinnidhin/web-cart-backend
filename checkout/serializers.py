from rest_framework import serializers

from cart.models import Cart
from products.serializers import ProductListCreateSerializer

class CheckoutSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request")

        if Cart.objects.filter(buyer = request.user, checked_out = True, product = validated_data["product"]):
            checkout = Cart.objects.get(buyer = request.user, checked_out = True, product = validated_data["product"])

            cart = Cart()
            cart.product = validated_data["product"]

            checkout.save()

        return checkout

    class Meta:
        product = ProductListCreateSerializer(read_only=True, many=True)
        model = Cart
        fields = ["product", "checked_out", "id", "delivery_status"]
        depth = 1

        