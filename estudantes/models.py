from django.db import models

# Criando o model para o CRUD.
class Estudante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.id}, {self.nome}, {self.curso}'