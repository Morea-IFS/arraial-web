from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class DeviceApplication(models.IntegerChoices):
    none = 0, 'Not Defined',
    dress = 1, 'Vestido',
    detonator = 2, 'Detonador',
    displays = 3, 'Displays'
    
class AuthTypes(models.IntegerChoices):
    pending = 0, 'Pending',
    notAuthorized = 1, 'Not Authorized',
    Authorized = 2, 'Authorized',

class User(AbstractUser):
    email = models.CharField(max_length=256, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
class Device(models.Model):
    name = models.CharField(max_length=255, null=True)
    application = models.IntegerField(
        choices=DeviceApplication.choices, default=DeviceApplication.none)
    is_authorized = models.IntegerField(choices=AuthTypes.choices, default=AuthTypes.pending)
    mac_address = models.CharField(
        max_length=255, null=True, blank=True, unique=True)
    ip_address = models.GenericIPAddressField(
        max_length=255, null=True, blank=True)
    api_token = models.CharField(
        max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Unnamed"