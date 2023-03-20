from django.shortcuts import render
from rest_framework import generics,permissions
from . models import Wishlist
from . serializers import WishlistListingSerializer, wishlistSerializer, WishlistDeleteSerializer
from . permissions import OwnerOrAdmin
# Create your views here.


class WishlistView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            wishlist = Wishlist.objects.all()
        
        else:
            wishlist = Wishlist.objects.filter(buyer = user)
        
        return wishlist
    serializer_class = wishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

class WishlistListing(generics.ListCreateAPIView):
    # def get_queryset(self):
    #     user = self.request.user
    #     wishlists = Wishlist.objects.filter(buyer = user)
    #     return wishlists
    queryset = Wishlist.objects.all()

    serializer_class = WishlistListingSerializer
    permission_classes = [OwnerOrAdmin]

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        wishlist = Wishlist.objects.filter(buyer = user)

        return wishlist
    serializer_class = WishlistListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class WishlistDelete(generics.DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]