from rest_framework import generics,permissions
from django.contrib.auth.models import User
from .serializers import AddressSerializer

class AddressList(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        address = user.address_set.all().order_by("-id")
        return address

    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

