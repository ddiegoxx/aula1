from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateTimeField("date published")