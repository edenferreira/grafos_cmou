from grafo import *

class dijkstra:
  
  def __init__(self,grafo):
    self.grafo = grafo
    self.nao_visitados = set(grafo.pontos)
    self.visitados = set()
    self.distancia = {}
    self.distancia_visitados = {}
    self.anterior = {}
    self.num_passos = 0
    self.executou = False
  
  def definir_origem_destino(self,ponto_origem,ponto_destino):
    self.ponto_origem = ponto_origem
    self.ponto_destino = ponto_destino
  
  def deve_atualizar_distancia(self,ponto_atual,ponto_alvo):
    return self.distancia[ponto_alvo] > self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo]
  
  def atualizar_distancia(self,ponto_atual,ponto_alvo):
    self.distancia[ponto_alvo] = self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo]
    self.anterior[ponto_alvo] = ponto_atual
  
  def ponto_visitado(self,ponto):
    return ponto in self.visitados
  
  def visitar_ponto(self,ponto_atual,ponto_alvo):
    if not self.ponto_visitado(ponto_alvo):
     if ponto_alvo not in self.distancia or self.deve_atualizar_distancia(ponto_atual,ponto_alvo):
       self.atualizar_distancia(ponto_atual,ponto_alvo)    
  
  def processar_arestas(self,ponto_atual):
    for ponto_alvo in self.grafo.arestas[ponto_atual]:
      self.visitar_ponto(ponto_atual,ponto_alvo)
  
  def processar_ponto(self,ponto_atual):
    self.processar_arestas(ponto_atual)
    self.distancia_visitados[ponto_atual] = self.distancia[ponto_atual]
    del self.distancia[ponto_atual]
    self.visitados.add(ponto_atual)
    self.nao_visitados.remove(ponto_atual)
  
  def buscar_proximo_ponto(self):
      return min(self.distancia, key=self.distancia.get)
  
  def buscar_origem(self):
    self.distancia[self.ponto_origem] = 0
    return self.ponto_origem
  
  def formatar_caminho(self):
    """recebe um dicionário de anteriores com menor caminho, e retorna
         apenas o caminho entre o ponto_origem e o ponto_destino"""
    self.caminho = list()
    ponto_atual = self.ponto_destino
    while True:
      self.caminho.insert(0,ponto_atual)
      if ponto_atual == self.ponto_origem:
        break
      ponto_atual = self.anterior[ponto_atual]
    
  def executar(self):
    ponto_atual = self.buscar_origem()
    while self.nao_visitados:
      self.processar_ponto(ponto_atual)
      if ponto_atual == self.ponto_destino: break
      ponto_atual = self.buscar_proximo_ponto()
      self.num_passos += 1
    self.formatar_caminho()
    self.distancia_total = self.distancia_visitados[self.ponto_destino]
    self.executou = True

class a_star(dijkstra):
  
  def __init__(self,grafo):
    self.distancia_prev = {}
    self.distancia_prev_fronteira = {}
    super(a_star,self).__init__(grafo)
    
  def atualizar_distancia(self,ponto_atual,ponto_alvo):
    self.distancia[ponto_alvo] = self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo]
    self.distancia_prev_fronteira[ponto_alvo] = self.distancia[ponto_atual] + self.grafo.pesos[ponto_atual,ponto_alvo] + self.distancia_prev[ponto_alvo]
    self.anterior[ponto_alvo] = ponto_atual
  
  def processar_arestas(self,ponto_atual):
    for ponto_alvo in self.grafo.arestas[ponto_atual]:
      self.distancia_prev[ponto_alvo] = self.grafo.calc_prev_peso(ponto_alvo,self.ponto_destino)
      self.visitar_ponto(ponto_atual,ponto_alvo)
  
  def processar_ponto(self,ponto_atual):
    self.distancia_prev[ponto_atual] = self.grafo.calc_prev_peso(ponto_atual,self.ponto_destino)
    self.processar_arestas(ponto_atual)
    self.distancia_visitados[ponto_atual] = self.distancia[ponto_atual]
    del self.distancia[ponto_atual]
    del self.distancia_prev_fronteira[ponto_atual]
    self.visitados.add(ponto_atual)
    self.nao_visitados.remove(ponto_atual)
  
  def buscar_proximo_ponto(self):
    return min(self.distancia_prev_fronteira, key=self.distancia_prev_fronteira.get)
  
  def buscar_origem(self):
    self.distancia[self.ponto_origem] = 0
    self.distancia_prev[self.ponto_origem] = self.grafo.calc_prev_peso(self.ponto_origem,self.ponto_destino)
    self.distancia_prev_fronteira[self.ponto_origem] = self.distancia_prev[self.ponto_origem]
    return self.ponto_origem
    
  