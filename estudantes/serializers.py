from rest_framework import serializers
from .models import Estudante

# Criando o serializer para gerar o create, update e delete do model
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = "__all__"