from pprint import pprint
from collections import defaultdict
import random as rnd
import math
import pickle as pc
import os

class Grafo:
  """Classe que mantém coleções de pontos, arestas, e seus atributos, como posições,
       pesos, direção"""

  def __init__(self,ident=0):
    self.ident = ident
    self.pontos = set()
    self.pos_pontos = defaultdict()
    self.arestas = defaultdict(list)
    self.arestas_chegando = defaultdict(list)
    self.pesos = {}
    self.num_arestas = 0

  def __len__(self):
    return len(self.pontos)

  def add_ponto(self,ponto,pos_x,pos_y):
    """adiciona ponto e a posição dele no plano"""
    self.pontos.add(ponto)
    self.pos_pontos[ponto] = (pos_x,pos_y)
  
  def add_aresta(self,de_ponto,para_ponto,peso,chance_dupla=0):
    """adiciona uma aresta saindo do ponto da esquerda para o ponto da direita
         com uma chance de adicionar uma na direção oposta se for passado o
         atributo"""    
    self.arestas[de_ponto].append(para_ponto)
    self.arestas_chegando[para_ponto].append(de_ponto)
    self.pesos[de_ponto,para_ponto] = peso
    self.num_arestas += 1
    if rnd.randint(1,100) <= chance_dupla:      
      self.arestas[para_ponto].append(de_ponto)
      self.arestas_chegando[de_ponto].append(para_ponto)
      self.pesos[para_ponto,de_ponto] = peso
      self.num_arestas += 1

  def calc_distancia(self,de_ponto,para_ponto):
    """calcula distância das duas arestas passadas"""
    cateto_1 = self.pos_pontos[para_ponto][0]-self.pos_pontos[de_ponto][0]
    cateto_2 = self.pos_pontos[para_ponto][1]-self.pos_pontos[de_ponto][1]
    return math.sqrt(((cateto_1)**2)+((cateto_2)**2))

  def calc_prev_peso(self,de_ponto,para_ponto):
    """preve o custo entre os dois pontos passados"""
    return self.calc_distancia(de_ponto,para_ponto)

  def calc_peso(self,de_ponto,para_ponto,velocidade=1):
    """calcula o peso baseado na distancia e velocidade passada"""
    return self.calc_distancia(de_ponto,para_ponto) / velocidade

  def criar_grafo_aleatoriamente(self,num_pontos,max_p):
    """cria um grafo aleatoriamente, baseado no número de pontos, tamanho do ciclo gerador, e se o grafo é apenas um ciclo ou não"""
    self.max_x = max_p
    self.max_y = max_p
    self.ciclo = False
    self.fra_ciclo = num_pontos // 100
    self.chance_dupla = 20

    for i in range(self.fra_ciclo):
      self.add_ponto(i,rnd.uniform(0,self.max_x),rnd.uniform(0,self.max_y))
    lista_pontos = list(self.pontos)
    rnd.shuffle(lista_pontos)
    
    for i in range(len(lista_pontos)-1):
      self.add_aresta(lista_pontos[i],lista_pontos[i+1],self.calc_peso(lista_pontos[i],lista_pontos[i+1]),self.chance_dupla)
    self.add_aresta(lista_pontos[-1],lista_pontos[0],self.calc_peso(lista_pontos[-1],lista_pontos[0]),self.chance_dupla)
    del lista_pontos
    if not self.ciclo:
      for ponto in range(self.fra_ciclo, num_pontos):
        self.add_ponto(ponto,rnd.uniform(0,self.max_x),rnd.uniform(0,self.max_y))
        de_ponto = rnd.randrange(0,len(self),1)
        para_ponto = rnd.randrange(0,len(self),1)
        if de_ponto == para_ponto:
          self.add_aresta(de_ponto,ponto,self.calc_peso(de_ponto,ponto),0)
          self.add_aresta(ponto,para_ponto,self.calc_peso(ponto,para_ponto),0)
        else:
          self.add_aresta(de_ponto,ponto,self.calc_peso(de_ponto,ponto),self.chance_dupla)
          self.add_aresta(ponto,para_ponto,self.calc_peso(ponto,para_ponto),self.chance_dupla)
  
  def criar_aleatoriamente_cidade(self,grid_x,grid_y,max_x,max_y,distancia_min):
    if grid_x > 1400 or grid_y > 1400:
      pass
    fracao_x = max_x  / grid_x
    fracao_y = max_y / grid_y
    
    self.max_x = max_x
    self.max_y = max_y
    
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

    for key_x,x in p_x.items():
      for key_y,y in p_y.items():
        self.add_ponto((key_x*1000000)+key_y,rnd.uniform(x[0],x[1]),rnd.uniform(y[0],y[1]))

    for i in range(grid_x - 1):
      for j in range(grid_y - 1):
        ponto_atual = (i*1000000)+j
        ponto_direita = (i*1000000)+j+1
        ponto_abaixo = ((i+1)*1000000)+j        
        #print(i,j,ponto_atual,ponto_direita,ponto_abaixo)
        if (i/1000000) % 2 == 0:
          self.add_aresta(ponto_atual,ponto_direita,self.calc_distancia(ponto_atual,ponto_direita),20)
        else:
          self.add_aresta(ponto_direita,ponto_atual,self.calc_distancia(ponto_direita,ponto_atual),20)
        if j % 2 == 0:
          self.add_aresta(ponto_abaixo,ponto_atual,self.calc_distancia(ponto_abaixo,ponto_atual),20)
        else:
          self.add_aresta(ponto_atual,ponto_abaixo,self.calc_distancia(ponto_atual,ponto_abaixo),20)

  def armazenar_grafo(self,diretorio):
    """cria diretorio passado caso ele não exista, e armazena o grafo com a identidade"""
    if not os.path.exists(diretorio):
      os.makedirs(diretorio)
    with open(diretorio + '\\grafo_'+str(self.ident)+'.p','wb') as arq:
      pc.dump(self,arq,4)
  
  def gerar_grafo_arquivo(self,path):
    """gera grafo a partir de um grafo em arquivo .p"""
    with open(path,'r') as arq:
      self = pc.load(arq)
