from django.db import models
from funcionario.models import Funcionario

# Create your models here.
class Ferramenta(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField(unique=True)
    quantidade = models.IntegerField()
    saida = models.IntegerField(default=0)

    def __str__(self):
        return self.nome