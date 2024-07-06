from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    votou = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Candidato(models.Model):
    candidato = models.CharField(max_length=100, unique=True)
    numero_candidato = models.IntegerField(validators=[MaxValueValidator(99),MinValueValidator(10)])
    votos_candidato = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return f"{self.candidato} - Número: {self.numero_candidato}"