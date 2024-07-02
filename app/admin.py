from django.contrib import admin
from .models import Device

# Register your models here.

class DevicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'application', 'mac_address', 'ip_address', 'is_authorized']
    
admin.site.register(Device, DevicesAdmin)