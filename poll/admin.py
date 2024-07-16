from django.contrib import admin
from . models import Aluno
from . models import Candidato
from . models import Candidata
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ('nome','matricula','turma','votou')
    search_fields = ('nome','matricula')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('candidato','numero_do_candidato','votos_do_candidato')
    search_fields = ('candidato','numero_do_candidato')

@admin.register(Candidata)
class CandidataAdmin(admin.ModelAdmin):
    list_display = ('candidata','numero_da_candidata','votos_da_candidata')
    search_fields = ('candidata','numero_da_candidata')

