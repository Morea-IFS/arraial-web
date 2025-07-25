from rest_framework import serializers
from .models import Dress

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ['effect', 'color', 'status']
        extra_kwargs = {
            'effect': {'required': True},
            'color': {'required': True},
            'status': {'required': True}
        }