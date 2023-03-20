from django.shortcuts import render
from rest_framework import generics, permissions, views, response
from checkout.permissions import OwnerOnly
from .models import Cart
from .serializers import CartDeleteSerializer, CartProductSerializer, CartSerializer, CartAdminSerializer, CartCountDecrementSerializer
from products.serializers import ProductListCreateSerializer
from .permissions import OwnerOrAdmin
from products.models import Product
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# listing the products

class CartList(generics.ListCreateAPIView):

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            carts = Cart.objects.all()
        
        else:
            carts = Cart.objects.filter(buyer = user, checked_out = False)
        
        return carts

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return CartAdminSerializer
        
        return CartSerializer 

    permission_classes = [permissions.IsAuthenticated]

#cart products count increment:-

class CartListItems(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [OwnerOrAdmin]

#cart products count decrement:-

class CartDecrement(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCountDecrementSerializer
    permission_classes = [OwnerOrAdmin]

#cart detail:-

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return CartAdminSerializer
        return CartSerializer
    
    permission_classes = [OwnerOrAdmin]

class CartDelete(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CartDeleteSerializer