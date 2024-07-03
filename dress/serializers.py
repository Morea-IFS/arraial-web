from rest_framework import serializers
from .models import Dress

class DressSerializer(serializers.Serializer):
    effect = serializers.IntegerField()
    
    class Meta:
        model = Dress
        