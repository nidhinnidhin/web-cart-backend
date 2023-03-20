from django.shortcuts import render
from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from . permissions import ListIsAdminOrReadOnly

# Create your views here.

class AnnouncementList(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [ListIsAdminOrReadOnly]