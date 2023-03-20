from django.shortcuts import render
from . models import Slider
from rest_framework import generics
from . serializers import SliderCreateSerializer
from . permissions import ListIsAdminOrReadOnly


# Create your views here.

class SliderListView(generics.ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderCreateSerializer
    permission_classes = [ListIsAdminOrReadOnly]
    
