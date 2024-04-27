from django.shortcuts import render
from rest_framework import viewsets
from estoque.models import LogSaida, LogEntrada
from estoque.api.serializers import LogSaidaSerializer, LogEntradaSerializer
# Create your views here.

class LogSaidaViewSet(viewsets.ModelViewSet):
    queryset = LogSaida.objects.all()
    serializer_class = LogSaidaSerializer

class LogEntradaViewSet(viewsets.ModelViewSet):
    queryset = LogEntrada.objects.all()
    serializer_class = LogEntradaSerializer
    