from collections import defaultdict
import grafo as gf
import random as rnd

def formatar_caminho(anterior,ponto_origem,ponto_destino):
  """recebe um dicionário de anteriores com menor caminho, e retorna
       apenas o caminho entre a origem e o destino"""
  caminho = list()
  ponto_atual = ponto_destino
  while True:
    caminho.insert(0,ponto_atual)
    if ponto_atual == ponto_origem:
      break
    ponto_atual = anterior[ponto_atual]
  return caminho

def dijkstra(grafo,ponto_origem,ponto_destino):
  """busca o menor caminho entre os os dois pontos passados num grafo"""
  pontos = list(grafo.pontos)
  nao_visitados = set(grafo.pontos)
  visitados = set()
  distancia = {}
  distancia_visitados = {}
  anterior = {}
  num_passos = 0
  
  ponto_atual = ponto_origem
  distancia[ponto_atual] = 0
  
  while nao_visitados:
    for para_ponto in grafo.arestas[ponto_atual]:
      if para_ponto not in visitados:
       if para_ponto not in distancia or distancia[para_ponto] > distancia[ponto_atual] + grafo.pesos[ponto_atual,para_ponto]:
         distancia[para_ponto] = distancia[ponto_atual] + grafo.pesos[ponto_atual,para_ponto]
         anterior[para_ponto] = ponto_atual

    distancia_visitados[ponto_atual] = distancia[ponto_atual]
    del distancia[ponto_atual]
    visitados.add(ponto_atual)
    nao_visitados.remove(ponto_atual)
    
    if ponto_atual == ponto_destino:
      break #encontrado destino
    ponto_atual = min(distancia, key=distancia.get)
    num_passos += 1
    
  caminho = formatar_caminho(anterior,ponto_origem,ponto_destino)
  del nao_visitados,visitados,distancia,anterior  
  
  return caminho,distancia_visitados[ponto_destino],num_passos

def a_star(grafo,ponto_origem,ponto_destino):
  """busca o menor caminho entre os os dois pontos passados num grafo
       usando de heurística, prevendo o menor caminho dos próximos pontos"""
  pontos = list(grafo.pontos)
  nao_visitados = set(grafo.pontos)
  visitados = set()
  distancia = {}
  distancia_prev = {}
  distancia_prev_fronteira = {}
  distancia_visitados = {}
  anterior = {}
  num_passos = 0

  ponto_atual = ponto_origem
  distancia[ponto_atual] = 0
  distancia_prev[ponto_atual] = grafo.calc_prev_peso(ponto_atual,ponto_destino)
  distancia_prev_fronteira[ponto_atual] = distancia_prev[ponto_atual]
  
  while nao_visitados:
    distancia_prev[ponto_atual] = grafo.calc_prev_peso(ponto_atual,ponto_destino)
    for para_ponto in grafo.arestas[ponto_atual]:
      distancia_prev[para_ponto] = grafo.calc_prev_peso(para_ponto,ponto_destino)
      if para_ponto not in visitados:
       if para_ponto not in distancia or distancia[para_ponto] > distancia[ponto_atual] + grafo.pesos[ponto_atual,para_ponto]:
         distancia[para_ponto] = distancia[ponto_atual] + grafo.pesos[ponto_atual,para_ponto]
         distancia_prev_fronteira[para_ponto] = distancia[ponto_atual] + grafo.pesos[ponto_atual,para_ponto] + distancia_prev[para_ponto]
         anterior[para_ponto] = ponto_atual

    distancia_visitados[ponto_atual] = distancia[ponto_atual]
    del distancia[ponto_atual]
    del distancia_prev_fronteira[ponto_atual]
    visitados.add(ponto_atual)
    nao_visitados.remove(ponto_atual)
    
    if ponto_atual == ponto_destino:
      break #encontrado destino

    ponto_atual = min(distancia_prev_fronteira, key=distancia_prev_fronteira.get)
    num_passos += 1

  caminho = formatar_caminho(anterior,ponto_origem,ponto_destino)
  del nao_visitados,visitados,distancia,anterior,distancia_prev_fronteira,distancia_prev

  return caminho,distancia_visitados[ponto_destino],num_passos
