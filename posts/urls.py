from django.urls import path
from . import views

# Dando um nome para nomear esse app daqui e quando for direcionar ter que colocar o posts/name. Com isso não conflitar com outras htmls
app_name = 'posts'

# Está começando com /posts (como está nas urls do project), por isso está com path vazio. Está pegando como base o /pots
urlpatterns = [
    path('', views.posts, name="home"),
]
