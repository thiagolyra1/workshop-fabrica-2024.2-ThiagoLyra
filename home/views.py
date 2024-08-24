from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):    
    context  = {
        'text': 'Olá, sou o Thiago de Lyra Borges. Seja bem-vindo ao meu projeto! Aqui, você encontrará uma view que consome dados de uma API e outra que implementa um CRUD simples. Explore as funcionalidades e sinta-se à vontade para experimentar! :)',
        'title': '',
    }
    
    return render(
        request,
        'home/index.html',
        context,
    )