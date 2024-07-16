from django.contrib import admin
from . models import Aluno
from . models import Candidato
from . models import Candidata
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ('nome','matricula','votou')
    search_fields = ('nome','matricula')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('candidato','numero_candidato','votos_candidato')
    search_fields = ('candidato','numero_candidato')

@admin.register(Candidata)
class CandidataAdmin(admin.ModelAdmin):
    list_display = ('candidata','numero_candidata','votos_candidata')
    search_fields = ('candidata','numero_candidata')

