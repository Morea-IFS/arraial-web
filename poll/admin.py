from django.contrib import admin
from . models import Aluno, Candidata, Candidato

# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ('nome','matricula','turma','votou','candidato','candidata')
    search_fields = ('nome','matricula')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('candidato','turma_candidato','numero_do_candidato','votos_do_candidato','foto_candidato','descricao_candidato')
    search_fields = ('candidato','numero_do_candidato')

@admin.register(Candidata)
class CandidataAdmin(admin.ModelAdmin):
    list_display = ('candidata','turma_candidata','numero_da_candidata','votos_da_candidata','foto_candidata','descricao_candidata')
    search_fields = ('candidata','numero_da_candidata')

