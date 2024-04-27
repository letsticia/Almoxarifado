from django.db import models
from funcionario.models import Funcionario
from ferramentas.models import Ferramenta
from django.utils import timezone

# Create your models here.

class LogSaida(models.Model):
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    entregue = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        
        self.ferramenta.saida += self.quantidade
        self.ferramenta.quantidade -= self.quantidade
        self.ferramenta.save()
        super(LogSaida, self).save(*args, **kwargs)

    def __str__(self):
        return f"Saida de {self.ferramenta.nome} - {self.quantidade} un. - {self.funcionario.nome}"
    
class LogEntrada(models.Model):
    LogSaida = models.ForeignKey(LogSaida, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.LogSaida.ferramenta.saida -= self.LogSaida.quantidade
        self.LogSaida.ferramenta.quantidade += self.LogSaida.quantidade
        self.LogSaida.entregue = True
        self.LogSaida.ferramenta.save()
        self.LogSaida.save()
        super(LogEntrada, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"Entrada de {self.LogSaida.ferramenta.nome} - {self.LogSaida.quantidade} un. - {self.LogSaida.funcionario.nome}"


    