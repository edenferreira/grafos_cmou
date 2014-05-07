from grafo import *
from caminhos_minimos import *

def execute():
  grafo = Grafo()
  grafo.criar_grafo_aleatoriamente(1000,1000)
  dij = dijkstra(grafo)
  dij.definir_origem_destino(0,900)
  dij.executar()
  print('%.2f : ' % dij.distancia_total,dij.num_passos,dij.caminho)

def execute_a():
  grafo = Grafo()
  grafo.criar_grafo_aleatoriamente(1000,1000)
  ast = a_star(grafo)
  ast.definir_origem_destino(0,900)
  ast.executar()
  print(ast.num_passos,ast.caminho)

for i in range(100):
  execute()
  
