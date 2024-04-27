from rest_framework import serializers
from estoque.models import LogSaida, LogEntrada
from ferramentas.api.serializers import FerramentaSerializer
from funcionario.api.serializers import FuncionarioSerializer

class LogSaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogSaida
        fields = ['ferramenta', 'funcionario', 'quantidade', 'data']
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['ferramenta'] = FerramentaSerializer(instance.ferramenta).data
        response['funcionario'] = FuncionarioSerializer(instance.funcionario).data
        response['entregue'] = instance.entregue
        return response


class LogEntradaSerializer(serializers.ModelSerializer):
    LogSaida = serializers.PrimaryKeyRelatedField(queryset=LogSaida.objects.all())

    class Meta:
        model = LogEntrada
        fields = ['LogSaida']
    
    def to_representation(self, instance):
        self.fields['LogSaida'] = serializers.PrimaryKeyRelatedField(queryset=LogSaida.objects.filter(entregue=False))
        response = super().to_representation(instance)
        response['ferramenta'] = FerramentaSerializer(instance.LogSaida.ferramenta).data
        response['funcionario'] = FuncionarioSerializer(instance.LogSaida.funcionario).data
        return response
