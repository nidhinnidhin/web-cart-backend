from rest_framework import serializers
from slider.models import Slider

class SliderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"