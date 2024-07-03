from django.db import models
from app.models import Device

# Create your models here.

class PinOptions(models.IntegerChoices):
    notSelected = 0, 'Not Selected'
    D1 = 1, 'D1'
    D2 = 2, 'D2'
    D3 = 3, 'D3'
    D4 = 4, 'D4'
    D5 = 5, 'D5'
    D6 = 6, 'D6'
    D7 = 7, 'D7'
    D8 = 8, 'D8'

class Detonador(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    pin = models.IntegerField(default=PinOptions.notSelected, choices=PinOptions.choices)
    status = models.BooleanField(default=False)