from django.db import models

# Create your models here.

class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    votou = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Voto(models.Model):
    voto = models.CharField(max_length=3)

    def __str__(self):
        return "Voto no Candidato {self.numero_candidato}"