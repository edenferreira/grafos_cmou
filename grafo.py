from collections import *
from random import *
import math

class Grafo:
  """Classe que mantém coleções de pontos, arestas, e seus atributos, como posições,
       pesos, direção"""

  def __init__(self):
    self.pontos = set()
    self.pos_pontos = defaultdict()
    self.arestas = defaultdict(list)
    self.pesos = {}
    self.num_arestas = 0
    
