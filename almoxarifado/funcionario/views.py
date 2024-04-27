from django.shortcuts import render
from funcionario.models import Funcionario
from rest_framework import viewsets
from funcionario.api.serializers import FuncionarioSerializer
# Create your views here.

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
