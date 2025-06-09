
from django.db import models
from app.models import Device

class DressEffects(models.IntegerChoices):
    off = 0, 'Desligado'
    rainbow = 1, 'Arco íris'
    fire = 2, 'Fogo'
    spectrum = 3, 'Espectro'
    heartbeat = 4, 'Pulsação'

class Dress(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, null=True, blank=True)
    effect = models.IntegerField(default=DressEffects.off, choices=DressEffects.choices)
    status = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.device.deviceName} - {self.get_effect_display()}"