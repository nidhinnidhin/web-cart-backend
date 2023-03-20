from django.shortcuts import render
from .models import Product
from rest_framework import generics,permissions
from .serializers import ProductListCreateSerializer
from .permissions import ListIsAdminOrReadOnly, ObjIsAdminOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListCreateSerializer
    permission_classes = [ListIsAdminOrReadOnly]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListCreateSerializer
    permission_classes = [ObjIsAdminOrReadOnly]

class ProductFilter(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListCreateSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']


