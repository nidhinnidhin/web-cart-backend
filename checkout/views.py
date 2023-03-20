from cart.models import Cart
from checkout.serializers import CheckoutSerializer
from products.models import Product
from address.models import Address
from . permissions import AdminOnly,OwnerOnly
from rest_framework import permissions,generics,response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

import stripe

class CartCheckoutView(APIView):
    def get(self, request, format=None):

        user = request.user

        print(user)

        cart_checkouts = Cart.objects.filter(buyer = user, checked_out = False).update(checked_out = True)

        return response.Response (cart_checkouts)
        
    permission_classes = [permissions.IsAuthenticated]

class CartCheckoutList(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user

        checkouts = Cart.objects.filter(buyer = user, checked_out = True)                     
        return checkouts

    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]
        


class TestCheckout(APIView):
    def get(self, request, format=None):
        print("Reached")
        stripe.api_key = 'sk_test_51LVzIiSHbelfXOXs1ho3iSSJYxD0r1uV1xJZQyz5z0ocBITBnaESKU0BUirvrqMsbruMAdCj424PaxU9iLPbOiOR002N9N1z9a'

        allProducts = Cart.objects.filter( buyer =  request.user, checked_out = False)
        total = 0

        for i in allProducts:
            total += i.product.price + i.count 

        print(total)
        
        intent = stripe.PaymentIntent.create(
            amount = total*100,
            currency = 'inr',
            metadata = {'userid' : request.user.id}
        )
        return JsonResponse({'client_secret': intent.client_secret})