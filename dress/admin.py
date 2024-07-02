from django.contrib import admin
from .models import Dress

# Register your models here.

class DressAdmin(admin.ModelAdmin):
    list_display = ['device', 'effect']
    
admin.site.register(Dress, DressAdmin)