from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudanteViewSet

# Criando a rota com o DefaultRouter
router = DefaultRouter()
router.register(r'estudantes', EstudanteViewSet)

app_name = 'estudantes'

urlpatterns = [
    path('', include(router.urls), name="home"),
]