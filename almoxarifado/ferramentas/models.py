from django.db import models

# Create your models here.
class Ferramenta(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField()
    quantidade = models.IntegerField()
    estoque = models.IntegerField()
    saida = models.IntegerField(default=0)
    

    def __str__(self):
        return self.nome
