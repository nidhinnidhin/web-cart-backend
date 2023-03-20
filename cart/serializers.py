from rest_framework import serializers
from .models import Cart
from products.serializers import ProductListCreateSerializer

# listing the products:-

class CartSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request')

        if Cart.objects.filter(buyer = request.user, product = validated_data["product"],
        checked_out = False).exists():
            cart = Cart.objects.get(buyer = request.user, product = validated_data["product"],
            checked_out = False)
            cart.count = cart.count+1
            cart.save()
        
        else:
            cart = Cart()
            cart.buyer = request.user
            cart.product = validated_data["product"]
            try:
                cart.count = validated_data["count"]
            except:
                pass

            cart.save()
        return cart

    class Meta:
        product = ProductListCreateSerializer(read_only=True, many=True)
        model = Cart
        fields = ["product","count","checked_out","id"]
        depth = 1

class CartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ["checked_out", "buyer"]


#cart products count increment:-

class CartProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request')

        if Cart.objects.filter(buyer = request.user, product = validated_data["product"],
        checked_out = False).exists():
            cart = Cart.objects.get(buyer = request.user, product = validated_data["product"],
            checked_out = False)
            cart.count = cart.count+1
            cart.save()
        
        else:
            cart = Cart()
            cart.buyer = request.user
            cart.product = validated_data["product"]
            try:
                cart.count = validated_data["count"]
            except:
                pass

            cart.save()
        return cart

    class Meta:
        product = ProductListCreateSerializer(read_only=True, many=True)
        model = Cart
        fields = ["product","count","checked_out"]

#cart products count decrement:-

class CartCountDecrementSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get('request')

        if Cart.objects.filter(buyer = request.user, product = validated_data["product"],
        checked_out = False).exists():
            cart = Cart.objects.get(buyer = request.user, product = validated_data["product"],
            checked_out = False)
            cart.count = cart.count-1
            cart.save()
        
        else:
            cart = Cart()
            cart.buyer = request.user
            cart.product = validated_data["product"]
            try:
                cart.count = validated_data["count"]
            except:
                pass

            cart.save()
        return cart

    class Meta:
        product = ProductListCreateSerializer(read_only=True, many=True)
        model = Cart
        fields = ["product","count","checked_out"]
        
# admin section:-       
 
class CartAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"