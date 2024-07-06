from django.contrib import admin
from . models import Aluno
from . models import Candidato
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula','votou')
    search_fields = ('nome','matricula')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('candidato','numero_candidato','votos_candidato')
    search_fields = ('candidato','numero_candidato')

