from django.db import models

# Create your models here.
class Ferramenta(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField(unique=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

class FerramentaEstoque(models.Model):
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE, to_field='codigo')
    saida = models.IntegerField(default=0)

    def __str__(self):
        return self.ferramenta.nome