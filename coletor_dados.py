from caminhos_minimos import *
from datetime import date
import grafo as gf
import pickle as pc
import random as rnd
import cProfile as cpr
import pstats as pst
from collections import OrderedDict

def get_ident():
  import os.path
  ident = 0
  if not os.path.isfile('ident_grafos.txt'):
    with open('ident_grafos.txt','w') as arq:
      print(ident,file=arq)
    return ident
  else:
    with open('ident_grafos.txt','r') as arq:
      lista = arq.readlines()
      ident = int(lista[-1]) + 1
    with open('ident_grafos.txt','a') as arq:
      print(ident,file=arq)
    return ident
    
def carregar_grafos():
  with open('grafos.txt','r') as arq:
    lista_path = arq.readlines()
  for path_grafo in lista_path:
    yield pc.load(path_grafo)

def coletar_dados_algoritmos(grafo):
  dados = OrderedDict()
  dados['ident_grafo'] = grafo.ident
  dados['num_pontos'] = len(grafo)
  dados['num_arestas'] = grafo.num_arestas
  dados['fracao_ciclo'] = grafo.fra_ciclo
  dados['chance_dupla'] = grafo.chance_dupla
  dados['max_x'] = grafo.max_x
  dados['max_y'] = grafo.max_y
  
  ponto_origem, ponto_destino = rnd.sample(grafo.pontos,2)
  while ponto_origem == ponto_destino:
    ponto_destino = rnd.sample(grafo.pontos,1)
  dados['ponto_origem'] = ponto_origem
  dados['ponto_destino'] = ponto_destino

  caminho,distancia,num_passos = dijkstra(grafo,ponto_origem,ponto_destino)
  dados['caminho_d'] = list(caminho)
  dados['distancia_d'] = distancia
  dados['num_passos_d'] = num_passos
  del caminho,distancia,num_passos

  caminho, distancia,num_passos = a_star(grafo,ponto_origem,ponto_destino)
  dados['caminho_a'] = list(caminho)
  dados['distancia_a'] = distancia
  dados['num_passos_a'] = num_passos
  del caminho,distancia,num_passos

  #colocados no final do dicionário, para principais informações ficarem no início
  dados['pos_pontos'] = grafo.pos_pontos
  dados['arestas'] = grafo.arestas
  dados['pesos'] = grafo.pesos

  return dados

def criar_grafo_executar_armazenar(num_pontos,max_x,max_y,fra_ciclo,chance_dupla):
  grafo = gf.Grafo(get_ident())
  grafo.criar_grafo_aleatoriamente(num_pontos,max_x,max_y,fra_ciclo,False,chance_dupla)
  dados_execucao = coletar_dados_algoritmos(grafo)
  diretorio = 'D:\\Dropbox\\Trabalho de Conclusão de Curso\\grafos_cmou'
  diretorio += '\\grafos_e_dados\\pontos_' + str(num_pontos) + '\\max_x_E_max_y_' + str(max_x) + '\\' + str(date.today())

  import os.path
  if not os.path.exists(diretorio):
      os.makedirs(diretorio)
  
  arquivo = diretorio + '\\grafo_' + str(grafo.ident) + '.txt'
  with open(arquivo,'w') as arq:
    for key, value in dados_execucao.items():
      print(key.rjust(14), ' : ', value,file=arq)
  return dados_execucao
  

def executar_coleta(num_iteracoes):
  """para passar mais facilmente para o profiler"""
  for i in range(num_iteracoes):
    for j in range(num_iteracoes):
      criar_grafo_executar_armazenar(10**(3+j),10**(3+i),10**(3+i),10,30)
