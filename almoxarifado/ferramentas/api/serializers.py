from rest_framework import serializers
from ferramentas.models import Ferramenta

class FerramentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ferramenta
        fields = '__all__'
        
# class FerramentaEstoqueSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FerramentaEstoque
#         fields = ('ferramenta', 'saida', 'funcionario')
    
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['ferramenta'] = FerramentaSerializer(instance.ferramenta).data
#         return response
    