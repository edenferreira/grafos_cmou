from pprint import pprint


def criar_aleatoriamente_cidade(self,grid_x,grid_y,max_x, max_y,distancia_min):
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
tamanho_total = 1000
tam_espaco = tamanho_total/1000

tam_min = 0.02
tam_max = tam_espaco-tam_min
print(tam_min,tam_max)

x_1 = tam_min
x_2 = tam_max
y_1 = tam_min
y_2 = tam_max
p_x = {}
p_y = {}
for i in range(1000):
  p_x[i] = (x_1,x_2)
  x_1 += tam_espaco
  x_2 += tam_espaco
for i in range(1000):
  p_y[i] = (y_1,y_2)
  y_1 += tam_espaco
  y_2 += tam_espaco

pos_pontos = {}

from random import uniform

for key_x, x in p_x.items():
  for key_y, y in p_y.items():
    pos_pontos[(key_x*1000)+key_y] = (uniform(x[0],x[1]),uniform(y[0],y[1]))


with open('pos_pontos.txt','w') as arq:
  pprint(pos_pontos,stream=arq)

from grafo import *

grafo = Grafo(0)
for key,value in pos_pontos.items():
  grafo.add_ponto(key,value[0],value[1])

for i in range(999):
  for j in range(999):
    ponto_atual = (i*1000)+j
    ponto_direita = (i*1000)+j+1
    ponto_abaixo = ((i+1)*1000)+j
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

