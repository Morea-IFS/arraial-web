from rest_framework import serializers
from .models import Detonador, PinOptions

class DetonadorSerializer(serializers.Serializer):
    pin = serializers.IntegerField()
    status = serializers.BooleanField()
    
    class Meta:
        model = Detonador
        