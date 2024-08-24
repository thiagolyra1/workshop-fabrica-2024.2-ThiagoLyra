# workshop-fabrica-2024.2-ThiagoLyra
Desafio para a Fábrica de Software - Backend. Feito por: Thiago de Lyra Borges

# Versões utilizadas
Python 3.11.2 - Django 5.1

# Introdução

Essa é uma aplicação django que permite que os usuários visualizem dados obtidos de uma API externa, enquanto as operações de CRUD são realizadas exclusivamente no app "Estudantes". Esse projeto oferece uma interface intuitiva e interativa para facilitar o acesso e a manipulação de informações, garantindo uma experiência de usuário fluida e responsiva em diferentes dispositivos. Infelizmente não consegui autenticar com o JWT, até cheguei a instalar e configurar, mas não soube como acessar com o token. E o Docker eu cheguei a dar uma breve pesquisada, mas de primeira vista parecia um processo longo e por não ter tanto tempo, optei por não implementar esse diferencial.

# Tutorial para executar a plicação
Passos e comandos

1. clonar o git: -> https://github.com/thiagolyra1/workshop-fabrica-2024.2-ThiagoLyra.git

2. cd workshop-fabrica-2024.2-ThiagoLyra

3. Criar o ambiente virtual: -> python -m venv venv

4. Ativar/Carregar o ambiente virtual: -> venv\Scripts\activate

5. Instalar o Django, DjangoRest Framakework e requests. (com a venv ativada): -> pip install django djangorestframework requests

6. Instalar whitenoise para pegar os arquivos staticos -> pip install whitenoise

7. Instalar mysqlclient -> pip install mysqlclient
8. Criar database no sql (utilizei o workbench) -> create database teste;
9. Usar essa database criada -> use teste;
10. **LEMBRAR DE CONFIGURAR NO settings.py SUA PORTA/USUÁRIO/SENHA.**

11. Coletar os arquivos staticos -> python manage.py collectstatic

12. Instalar mysqlclient -> pip install mysqlclient
13. Criar database no sql (utilizei o workbench) -> create database teste;
14. Usar essa database criada -> use teste;
15. **LEMBRAR DE CONFIGURAR NO settings.py SUA PORTA/USUÁRIO/SENHA.**

16. Criar novas migrações com base nas alterações feitas nos modelos: -> python manage.py makemigrations

17. Aplicar e cancelar a aplicação de migrações: -> python manage.py migrate

18. Rodar o servidor: python manage.py runserver

