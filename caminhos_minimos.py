from grafo import *
from profilehooks import profile

class Caminho_Minimo:
  
  def __init__(self,grafo,a_star=False):
    self.grafo = grafo
    self.nao_visitados = set(grafo.pontos)
    self.visitados = set()
    self.distancia = {}
    self.distancia_visitados = {}
    self.anterior = {}
    self.num_passos = 0
    self.executou = False
    self.distancia_prev = {}
    self.distancia_prev_fronteira = {}
    self.a_star = a_star
  
  def definir_origem_destino(self,ponto_origem,ponto_destino):
    self.ponto_origem = ponto_origem
    self.ponto_destino = ponto_destino
  
  def buscar_origem(self):
    self.distancia[self.ponto_origem] = 0
    self.distancia_prev[self.ponto_origem] = self.grafo.calc_prev_peso(self.ponto_origem,self.ponto_destino)
    self.distancia_prev_fronteira[self.ponto_origem] = self.distancia_prev[self.ponto_origem]
    return self.ponto_origem
  
  def buscar_proximo_ponto(self):
    ponto_min = float("inf")
    val_min = float("inf")
    for elemento, valor in self.distancia_prev_fronteira.items():
      if valor < val_min:
        val_min = valor
        ponto_min = elemento
    return ponto_min
    #return min(self.distancia_prev_fronteira, key=self.distancia_prev_fronteira.get)
  
  def ponto_visitado(self,ponto):
    return ponto in self.visitados
  
  def processar_arestas(self,ponto_atual):
    for ponto_alvo in self.grafo.arestas[ponto_atual]:
      self.distancia_prev[ponto_alvo] = self.grafo.calc_prev_peso(ponto_alvo,self.ponto_destino)
      if not self.ponto_visitado(ponto_alvo):
        if ponto_alvo not in self.distancia or self.distancia[ponto_alvo] > self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo]:
          self.distancia[ponto_alvo] = self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo]
          if self.a_star:
            self.distancia_prev_fronteira[ponto_alvo] = self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo] + self.distancia_prev[ponto_alvo]
          else:
            self.distancia_prev_fronteira[ponto_alvo] = self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo]
          self.anterior[ponto_alvo] = ponto_atual

  def executar(self):
    ponto_atual = self.buscar_origem()
    while self.nao_visitados:
      self.distancia_prev[ponto_atual] = self.grafo.calc_prev_peso(ponto_atual,self.ponto_destino)
      self.processar_arestas(ponto_atual)
      self.distancia_visitados[ponto_atual] = self.distancia[ponto_atual]
      del self.distancia[ponto_atual]
      del self.distancia_prev_fronteira[ponto_atual]
      self.visitados.add(ponto_atual)
      self.nao_visitados.remove(ponto_atual)
      if ponto_atual == self.ponto_destino: break
      ponto_atual = self.buscar_proximo_ponto()
      self.num_passos += 1
    self.formatar_caminho()
    self.distancia_total = self.distancia_visitados[self.ponto_destino]
    self.executou = True
  
  def formatar_caminho(self):
    self.caminho = list()
    ponto_atual = self.ponto_destino
    while True:
      self.caminho.insert(0,ponto_atual)
      if ponto_atual == self.ponto_origem:
        break
      ponto_atual = self.anterior[ponto_atual]
