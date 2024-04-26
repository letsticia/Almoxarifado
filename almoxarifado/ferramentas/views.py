from django.shortcuts import render
from rest_framework import viewsets
from ferramentas.models import Ferramenta, FerramentaEstoque
from ferramentas.api.serializers import FerramentaSerializer, FerramentaEstoqueSerializer

# Create your views here.
class FerramentaViewSet(viewsets.ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer

class FerramentaEstoqueViewSet(viewsets.ModelViewSet):
    queryset = FerramentaEstoque.objects.all()
    serializer_class = FerramentaEstoqueSerializer
    