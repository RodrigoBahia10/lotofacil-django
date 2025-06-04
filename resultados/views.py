from django.shortcuts import render

# Create your views here.
# resultados/views.py

import requests
from django.shortcuts import render

# URL da API da Caixa para os resultados da Lotofácil
URL_API_LOTOFACIL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/"

def buscar_ultimo_resultado():
    """Busca os dados do último concurso e os retorna."""
    try:
        response = requests.get(URL_API_LOTOFACIL, timeout=10)
        response.raise_for_status() 
        dados = response.json()
        
        # Ordena as dezenas para exibição
        if dados and 'listaDezenas' in dados:
            dados['listaDezenas'] = sorted(dados['listaDezenas'], key=int)
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
        return None

def pagina_inicial(request):
    """
    Esta é a view para a nossa página inicial.
    Ela busca os dados e renderiza o template HTML.
    """
    # Chama a função auxiliar para buscar os dados
    dados_concurso = buscar_ultimo_resultado()
    
    # Cria um 'contexto', que é um dicionário de dados a serem enviados para o template
    context = {
        'concurso': dados_concurso
    }
    
    # Renderiza o template 'resultados/index.html' e passa o contexto para ele
    return render(request, 'resultados/index.html', context)