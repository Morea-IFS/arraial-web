from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status
import uuid
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginAuth
from .models import Device


# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        print(email, password)

        user = authenticate(request, email=email, password=password)
        
        print(user)

        if user is not None:
            loginAuth(request, user)

            try:
                return redirect("/dashboard")
            except:
                return redirect('/')
        else:
            return render(request, 'login.html', {'invalid': 'Usuário ou senha inválidos'})
            

    return render(request, 'login.html')

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

            return Response({'api_token': apiToken, 'id': device.id, 'deviceName': device.name}, status=status.HTTP_200_OK)
        else:
            apiToken = uuid.uuid4()

            try:
                newDevice = Device(mac_address=macAddress, ip_address=deviceIp, api_token=apiToken)
                newDevice.save()
            except:
                return Response({'error': 'something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)
            
            device = Device.objects.get(api_token=apiToken)

            return Response({'api_token': apiToken, 'id': device.id}, status=status.HTTP_201_CREATED)