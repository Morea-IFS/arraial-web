from django.db import models
from app.models import Device

class DressEffects(models.IntegerChoices):
    off = 0, 'Desligado'
    rainbow = 1, 'Arco íris'

# Create your models here.

class Dress(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    effect = models.IntegerField(default=DressEffects.off, choices=DressEffects.choices)