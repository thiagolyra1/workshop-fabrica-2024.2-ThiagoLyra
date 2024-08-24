from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Posts

# Create your views here.

def posts(request):
    jsonplaceholderAPI = requests.get(f'https://jsonplaceholder.typicode.com/posts')
    data = jsonplaceholderAPI.json()
    
    context  = {
        'text': 'Desenvolvi esta view para consumir os dados gratuitos disponíveis em: https://jsonplaceholder.typicode.com/. Abaixo, você encontrará os 100 posts disponíveis dessa API. Detalhe, esta view é responsiva! :)',
        'title': 'Posts - ',
        'posts': data,
    }
        
    return render(
        request,
        'posts/index.html',
        context,
    ) 