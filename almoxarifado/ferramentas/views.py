from django.shortcuts import render
from rest_framework import viewsets
from ferramentas.models import Ferramenta
from ferramentas.api.serializers import FerramentaSerializer

# Create your views here.
class FerramentaViewSet(viewsets.ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer