
from django.shortcuts import render
from .models import Dress, DressEffects
from rest_framework.decorators import api_view
from .serializers import DressSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    dress_data = Dress.objects.select_related('device').filter(
        device__is_authorized=2,
        device__application=1
    )
    dress_effects = DressEffects.choices
    
    if request.method == 'POST':
        device_id = request.POST.get('deviceId')
        effect = request.POST.get('effect')
        
        dress = Dress.objects.get(device__id=device_id)
        dress.effect = effect
        dress.status = effect != '0'
        dress.save()
    
    return render(request, 'dashboard/dress.html', {
        'dressData': dress_data,
        'dressEffects': dress_effects
    })

@api_view(['GET'])
def getEffect(request, pk):
    try:
        dress = Dress.objects.select_related('device').get(device__id=pk)
        return JsonResponse({
            'status': dress.effect,
            'active': dress.status
        })
    except Dress.DoesNotExist:
        return JsonResponse({'error': 'Device not found'}, status=404)