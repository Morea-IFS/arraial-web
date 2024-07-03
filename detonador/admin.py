from django.contrib import admin
from .models import Detonador

# Register your models here.

class DetonadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'device', 'pin', 'status']
    
admin.site.register(Detonador, DetonadorAdmin)