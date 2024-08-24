from django.urls import path
from . import views


# Dando um nome para nomear esse app daqui e quando for direcionar ter que colocar o posts/name. Com isso não conflitar com outras htmls
app_name = 'home'

# página inicial  
urlpatterns = [
    path('', views.home, name="home"),
]
