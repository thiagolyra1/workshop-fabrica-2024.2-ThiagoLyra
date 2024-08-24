from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Posts

# Função para a view dos posts, consumindo a API do endereço http e filtrando o seu json para ser utilizao no projeto.
def posts(request):
    jsonplaceholderAPI = requests.get(f'https://jsonplaceholder.typicode.com/posts')
    Posts.data = jsonplaceholderAPI.json()
    
    context  = {
        'text': 'Desenvolvi esta view para consumir os dados gratuitos disponíveis em: https://jsonplaceholder.typicode.com/. Abaixo, você encontrará os 100 posts disponíveis dessa API. Detalhe, esta view é responsiva! :)',
        'title': 'Posts - ',
        'posts': Posts.data,
    }
        
    return render(
        request,
        'posts/index.html',
        context,
    ) 