from django.urls import path
from . import views


# Nomeando esse app  para quando for direcionar ter que colocar o posts/name. Com isso não conflitar com outros arquivos htmls, caso tenha o mesmo nome em outro app
app_name = 'home'

# página inicial, pois está configurando com o path('') também na urls do project  
urlpatterns = [
    path('', views.home, name="home"),
]
