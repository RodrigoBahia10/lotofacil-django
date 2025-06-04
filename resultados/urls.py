# resultados/urls.py

from django.urls import path
from . import views # Importa as views do app atual

# Define um nome para o conjunto de URLs deste app, para evitar conflitos
app_name = 'resultados'

urlpatterns = [
    # Quando a URL raiz do app for acessada, chame a view 'pagina_inicial'
    path('', views.pagina_inicial, name='pagina_inicial'),
]