from django.shortcuts import render
from rest_framework import viewsets
from .models import Estudante
from .serializers import EstudanteSerializer

# Create your views here.
class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer