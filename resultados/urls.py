# resultados/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Importa as views do app atual

# Define um nome para o conjunto de URLs deste app, para evitar conflitos
app_name = 'resultados'

urlpatterns = [
    # Quando a URL raiz do app for acessada, chame a view 'pagina_inicial'
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('login/', auth_views.LoginView.as_view(template_name='resultados/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]