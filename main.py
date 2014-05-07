from grafo import *
from caminhos_minimos import *

def execute():
  grafo = Grafo()
  grafo.criar_grafo_aleatoriamente(1000,1000)
  dij = dijkstra(grafo)
  dij.definir_origem_destino(0,900)
  dij.executar()
  ast = a_star(grafo)
  ast.definir_origem_destino(0,900)
  ast.executar()
  #print('%.2f : ' % dij.distancia_total,dij.num_passos,dij.caminho)
  #print('%.2f : ' % ast.distancia_total,ast.num_passos,ast.caminho)
  with open('testando.txt','a') as arq:
    print(ast.caminho == dij.caminho,end='        ',file=arq)

for i in range(10):
  execute()
