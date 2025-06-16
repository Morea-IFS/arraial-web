from django.db import models
from app.models import Device

class DressEffects(models.IntegerChoices):
    OFF = 0, 'Desligado'
    STATIC = 1, 'Estático'
    BLINK = 2, 'Piscar'
    SNAKE = 3, 'Cobrinha'
    RAINBOW = 4, 'Arco-íris'
    FIRE = 5, 'Fogo'
    SPECTRUM = 6, 'Espectro'

class Dress(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    effect = models.IntegerField(
        choices=DressEffects.choices,
        default=DressEffects.OFF
    )
    color = models.CharField(max_length=7, default='#FF0000')
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.status = (self.effect != DressEffects.OFF)  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.device.id} - {self.get_effect_display()}"