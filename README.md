# workshop-fabrica-2024.2-ThiagoLyra
Desafio para a Fábrica de Software - Backend. Feito por: Thiago de Lyra Borges

# Versões utilizadas
Python 3.11.2 - Django 5.1

# Introdução

Essa é uma aplicação django que permite que os usuários visualizem dados obtidos de uma API externa, enquanto as operações de CRUD são realizadas exclusivamente no app "Estudantes". Esse projeto oferece uma interface intuitiva e interativa para facilitar o acesso e a manipulação de informações, garantindo uma experiência de usuário fluida e responsiva em diferentes dispositivos.

# Tutorial para executar a plicação
Passos e comandos

1. clonar o git: -> https://github.com/thiagolyra1/workshop-fabrica-2024.2-ThiagoLyra.git

2. Criar o ambiente virtual: -> python -m venv venv

3. Ativar/Carregar o ambiente virtual: -> venv\Scripts\activate

4. Instalar o Django, DjangoRest Framakework e requests. (com a venv ativada): -> pip install django djangorestframework requests

5. Instalar whitenoise para pegar os arquivos staticos -> pip install whitenoise

6. Coletar os arquivos staticos -> python manage.py collectstatic

7. Criar novas migrações com base nas alterações feitas nos modelos: -> python manage.py makemigrations

8. Aplicar e cancelar a aplicação de migrações: -> python manage.py migrate

9. Rodar o servidor: python manage.py runserver

