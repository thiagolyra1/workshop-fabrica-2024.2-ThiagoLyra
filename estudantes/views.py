from django.shortcuts import render
from rest_framework import viewsets
from .models import Estudante
from .serializers import EstudanteSerializer

# Criando a view com o "viewsets" para receber os objetos.
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer