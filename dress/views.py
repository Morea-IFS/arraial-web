from django.shortcuts import render
from .models import Dress, DressEffects

# Create your views here.

def index(request):
    dressData = Dress.objects.select_related('device').filter(device__is_authorized= 2)
    dressEffects = DressEffects.choices
    
    if request.method == 'POST':
        deviceId = request.POST.get('deviceId')
        effect = request.POST.get('effect')
        
        dress = Dress.objects.get(id=deviceId)
        
        dress.effect = effect
        dress.save()
    
    return render(request, 'dashboard/dress.html', {'dressData': dressData, 'dressEffects': dressEffects})

def getEffect(request, pk):
    print(pk)