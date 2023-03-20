from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ["fullName", "addressLine1", "addressLine2", "city", "country", "pincode", "mobile"]

    def create(self, validated_data):
        request = self.context.get('request')

        address = Address()

        address.owner = request.user
        address.fullName = validated_data["fullName"]
        address.addressLine1 = validated_data["addressLine1"]
        address.addressLine2 = validated_data["addressLine2"]
        address.city = validated_data["city"]
        address.country = validated_data["country"]
        address.pincode = validated_data["pincode"]
        address.mobile = validated_data["mobile"]

        address.save()

        return address