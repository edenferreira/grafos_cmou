from random import uniform
from pprint import pprint


def criar_aleatoriamente_cidade(self,grid_x,grid_y,max_x, max_y,distancia_min):
  if grid_x > 1400 or grid_y > 1400:
      """faça algo"""
  fracao_x = max_x  / grid_x
  fracao_y = max_y / grid_y

  tam_min_x = distancia_min / 2
  tam_max_x = fracao_x - tam_min_x
  tam_min_y = distancia_min / 2
  tam_max_y = fracao_y - tam_min_y

  x_1 = tam_min_x
  x_2 = tam_max_x
  y_1 = tam_min_y
  y_2 = tam_max_y
  p_x = {}
  p_y = {}
  for i in range(grid_x):
    p_x[i] = (x_1,x_2)
    x_1 += fracao_x
    x_2 += fracao_x
  for i in range(grid_y):
    p_y[i]  = (y_1,y_2)
    y_1 += fracao_y
    y_2 += fracao_y

  pos_pontos = {}

  for key_x,x in o_x.items():
    for key_y,y in p_y.items():
      self.add_ponto((key_x*1000000)+key_y,uniform(x[0],x[1]),uniform(y[0],y[1]))

  for i in range(grid_x - 1):
    for j in range(grid_y - 1):
      ponto_atual = (i*1000000)+j
      ponto_direita = (i*1000000)+j+1
      ponto_abaixo = ((i+1)*1000000)+j
    if (i/1000000) % 2 == 0:
      grafo.add_aresta(ponto_atual,ponto_direita,grafo.calc_distancia(ponto_atual,ponto_direita),20)
    else:
      grafo.add_aresta(ponto_direita,ponto_atual,grafo.calc_distancia(ponto_direita,ponto_atual),20)
    if j % 2 == 0:
      grafo.add_aresta(ponto_abaixo,ponto_atual,grafo.calc_distancia(ponto_abaixo,ponto_atual),20)
    else:
      grafo.add_aresta(ponto_atual,ponto_abaixo,grafo.calc_distancia(ponto_atual,ponto_abaixo),20)

for i in range(999):
  for j in range(999):
    ponto_atual = (i*1000000)+j
    ponto_direita = (i*1000000)+j+1
    ponto_abaixo = ((i+1)*1000000)+j
    if (i/1000) % 2 == 0:
      grafo.add_aresta(ponto_atual,ponto_direita,grafo.calc_distancia(ponto_atual,ponto_direita),10)
    else:
      grafo.add_aresta(ponto_direita,ponto_atual,grafo.calc_distancia(ponto_direita,ponto_atual),10)
    if j % 2 == 0:
      grafo.add_aresta(ponto_abaixo,ponto_atual,grafo.calc_distancia(ponto_abaixo,ponto_atual),10)
    else:
      grafo.add_aresta(ponto_atual,ponto_abaixo,grafo.calc_distancia(ponto_atual,ponto_abaixo),10)

with open('arestas.txt','w') as arq:
  pprint(grafo.arestas,stream = arq)



#with open('ponto_x.txt','w') as arq:
#  pprint(p_x,stream=arq)

#with open('ponto_y.txt','w') as arq:
#  pprint(p_y,stream=arq)

