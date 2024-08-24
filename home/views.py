from django.http import HttpResponse
from django.shortcuts import render

# Função para a view da página inicial, pois está configurada com path('') da aplicação principal.
def home(request):    
    context  = {
        'text': 'Olá, sou o Thiago de Lyra Borges. Seja bem-vindo ao meu projeto!',
        'title': '',
    }
    
    return render(
        request,
        'home/index.html',
        context,
    )