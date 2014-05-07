from grafo import *
from caminhos_minimos import *

def execute():
  grafo = Grafo()
  grafo.criar_grafo_aleatoriamente(1000,1000)
  dij = dijkstra(grafo)
  dij.definir_origem_destino(0,900)
  dij.executar()
  print(dij.num_passos,dij.caminho)

for i in range(10):
  execute()
  
