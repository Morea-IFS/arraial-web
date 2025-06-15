from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .models import Dress, DressEffects

@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        device_id = request.POST.get('deviceId')
        effect = int(request.POST.get('effect', DressEffects.OFF))  
        color = request.POST.get('color', '#FF0000')
        
        dress, created = Dress.objects.get_or_create(device_id=device_id)
        dress.effect = effect
        dress.color = color
        dress.save()
        return redirect('dress_dashboard')

    dress_data = Dress.objects.select_related('device').filter(
        device__is_authorized=2,
        device__application=1
    )
    return render(request, 'dashboard/dress.html', {
        'dressData': dress_data,
        'dressEffects': DressEffects.choices
    })

@api_view(['GET'])
def getEffect(request, pk):
    try:
        dress = Dress.objects.get(device_id=pk)
        return JsonResponse({
            'effect': dress.effect,
            'color': dress.color,
            'active': dress.status,
            'debug': f"Effect: {dress.get_effect_display()}, Color: {dress.color}"
        })
    except Dress.DoesNotExist:
        dress = Dress.objects.create(device_id=pk, effect=DressEffects.OFF)  
        return JsonResponse({
            'effect': DressEffects.OFF,
            'color': '#FF0000',
            'active': False
        })