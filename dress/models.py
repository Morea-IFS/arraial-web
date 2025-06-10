from django.db import models
from app.models import Device

class DressEffects(models.IntegerChoices):
    off = 0, 'Desligado'
    rainbow = 1, 'Arco íris'
    fire = 2, 'Fogo'
    spectrum = 3, 'Espectro'
    heartbeat = 4, 'Pulsação'
    other = 5, 'água'

class Dress(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    effect = models.IntegerField(
        choices=DressEffects.choices,
        default=DressEffects.off
    )
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.status = (self.effect != 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.device.id} - {self.get_effect_display()}"