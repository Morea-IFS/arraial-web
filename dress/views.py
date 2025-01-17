from django.shortcuts import render
from .models import Dress, DressEffects
from rest_framework.decorators import api_view
from .serializers import DressSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def index(request):
    dressData = Dress.objects.select_related('device').filter(device__is_authorized= 2).filter(device__application=1)
    dressEffects = DressEffects.choices
    
    if request.method == 'POST':
        deviceId = request.POST.get('deviceId')
        effect = request.POST.get('effect')
        
        dress = Dress.objects.get(id=deviceId)
        
        dress.effect = effect
        dress.save()
    
    return render(request, 'dashboard/dress.html', {'dressData': dressData, 'dressEffects': dressEffects})

@api_view(['GET'])
def getEffect(request, pk):
    dress = Dress.objects.select_related('device').get(device__id=pk)
    
    return JsonResponse(DressSerializer(dress).data, safe=False)