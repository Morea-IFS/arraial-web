from django.shortcuts import render
from .models import Detonador
from app.models import Device
from rest_framework.decorators import api_view
from .serializers import DetonadorSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def index(request):
    detonadorData = Detonador.objects.select_related('device').filter(device__is_authorized=2).filter(device__application=2)

    if request.method == "POST":
        deviceId = request.POST.get('deviceId')
        pinList = list(request.POST)[2:]
        
        device = Device.objects.get(id=deviceId)
        devicePinList = list(Detonador.objects.values_list('id', flat=True).filter(device=device))
        
        for x in devicePinList:
            detonadorUpdateObject = Detonador.objects.get(id=x)
            if str(x) in pinList:
                detonadorUpdateObject.status = True
                detonadorUpdateObject.save()
            else: 
                detonadorUpdateObject = Detonador.objects.get(id=x)
                detonadorUpdateObject.status = False
                detonadorUpdateObject.save()
                    
    return render(request, 'dashboard/detonador.html', {'detonadorData': detonadorData})

@api_view(['GET'])
def getStatus(request, pk):
    detonador = Detonador.objects.select_related('device').filter(device__id=pk)
    
    print(detonador)
    
    return JsonResponse(DetonadorSerializer(detonador, many=True).data, safe=False)