import grafo as gf
from caminhos_minimos import *

for k in range(50):
        for j in range(10):	
                with open('testando_grafos_%d.txt' % j,'w') as arq:
                        for i in range(100):
                                grafo = gf.Grafo(i)
                                grafo.criar_grafo_aleatoriamente(1000,10000,10000)
                                caminho_1, distancia_1 = dijkstra(grafo,0,1)
                                print(caminho_1,distancia_1,file=arq)
                                caminho_2, distancia_2 = a_star(grafo,0,1)
                                print(caminho_2,distancia_2,'\niguais? ',caminho_1 == caminho_2,end='\n\n',file=arq)

        lista = list()

        for j in range(10):
                with open('testando_grafos_%d.txt' % j,'r') as arq:
                        lista += arq.readlines()

        with open('resultado_%d.txt' % k,'w') as f:
                for i in range(len(lista)):
                        print(lista[i],file=f)
        del lista
