from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    turma = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(1)])
    candidato = models.IntegerField(default=0, editable=False)
    candidata = models.IntegerField(default=0, editable=False)
    votou = models.BooleanField(default=False,editable=False)

    def __str__(self):
        return self.nome
    
class Candidato(models.Model):
    
    candidato = models.CharField(max_length=100, unique=True, blank=False)
    foto_candidato = models.ImageField(upload_to='foto_candidato/', default='defaults/profile_default.png', blank=True)
    turma_candidato = models.IntegerField(default=0,validators=[MaxValueValidator(3),MinValueValidator(1)])
    descricao_candidato = models.CharField(max_length=256, blank=True)
    numero_do_candidato = models.IntegerField(validators=[MaxValueValidator(99),MinValueValidator(10)], blank=False)
    votos_do_candidato = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.candidato} - Número: {self.numero_do_candidato}"
    
class Candidata(models.Model):
    
    candidata = models.CharField(max_length=100, unique=True, blank=False)
    foto_candidata = models.ImageField(upload_to='foto_candidata/', default='defaults/profile_default.png', blank=True)
    turma_candidata = models.IntegerField(default=0,validators=[MaxValueValidator(3),MinValueValidator(1)])
    descricao_candidata = models.CharField(max_length=256, blank=True)
    numero_da_candidata = models.IntegerField(validators=[MaxValueValidator(99),MinValueValidator(10)], blank=False)
    votos_da_candidata = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.candidata} - Número: {self.numero_da_candidata}"