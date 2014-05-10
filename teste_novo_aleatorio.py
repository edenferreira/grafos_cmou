from cProfile import *
from grafo import *
from pprint import pprint

grafo = Grafo(0)
#grafo.criar_aleatoriamente_cidade(1000,900,900,1000,0.04)
#pprint(grafo.arestas,stream=open('grafo_teste_arestas.txt','w'))
#pprint(grafo.pos_pontos,stream=open('grafo_teste_pontos.txt','w'))

run('grafo.criar_aleatoriamente_cidade(%d,%d,%d,%d,%f)' % (1000,900,900,1000,0.04),'profiler')



with open('status_novo_aleatorio.txt','w') as arq:
  dados_crus = pst.Stats('profiler',stream=arq)
  dados_crus.strip_dirs().sort('cumtime').print_stats(10)
