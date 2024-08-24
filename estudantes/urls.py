from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudanteViewSet

# Criando os caminhos https e incluindo as urls de cada app.
router = DefaultRouter()
router.register(r'estudantes', EstudanteViewSet)

app_name = 'estudantes'
urlpatterns = [
    path('', include(router.urls), name="home"),
]