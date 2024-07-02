from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status
import uuid
from .models import Device


# Create your views here.


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# API

@api_view(['POST'])
def authenticateDevice(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        macAddress = data['macAddress']
        deviceIp = data['deviceIp']
        

        if Device.objects.all().filter(mac_address=macAddress).exists():
            apiToken = uuid.uuid4()

            device = Device.objects.get(mac_address=macAddress)
            device.api_token = str(apiToken)
            device.save()

            return Response({'api_token': apiToken, 'deviceName': device.name}, status=status.HTTP_200_OK)
        else:
            apiToken = uuid.uuid4()

            try:
                newDevice = Device(mac_address=macAddress, ip_address=deviceIp, api_token=apiToken)
                newDevice.save()
            except:
                return Response({'error': 'something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'api_token': apiToken}, status=status.HTTP_201_CREATED)