from rest_framework import generics,permissions
from django.contrib.auth.models import User
from .serializers import AddressSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address

class AddressList(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        address = user.address_set.all().order_by("-id")
        return address

    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressEditView(APIView):
    def put(self, request):
        user = self.request.user
        user.fullName = request.data["fullname"]
        user.addressLine1 = request.data["addressline1"]
        user.addressLine2 = request.data["addressline2"]
        user.city = request.data["city"]
        user.country = request.data["country"]
        user.pincode = request.data["pincode"]
        user.mobile = request.data["mobile"]

        user.save()

        return Response({"status": "Success"})
    
    permission_classes = [permissions.IsAuthenticated]

class AddressDetailView(APIView):
    def get(self,request):
        user = self.request.user.Address
        data = {
            "fullname":user.fullName,
            "addressline1": user.addressLine1,
            "addressline2": user.addressLine2,
            "city": user.city,
            "country": user.country,
            "pincode": user.pincode,
            "mobile": user.mobile,
        }
        return Response(data)
    permission_classes = [permissions.IsAuthenticated]