import sqlite3 as sql

class conexao:
  
  def __init__(self):
    self.banco = 'grafo_db'
  
  def __str__(self):
    return self.banco

  def iniciar_ident(self):
    comando_sql = """delete from ident_grafo"""
    con = sql.connect(self.banco)
    con.execute(comando_sql)
    con.commit()
    print("Iniciada tabela de identificação de grafos")
    con.close()

  def get_ident(self):
    comando_sql = """insert into ident_grafo(dump) values(0);"""
    con = sql.connect(self.banco)
    con.execute(comando_sql)
    con.commit()
    con.close()
    
    comando_sql = """select max(id) from ident_grafo;"""
    con = sql.connect(self.banco)
    lista = self.get_lista_de_cursor(con.execute(comando_sql))
    con.close()
    return lista

  def criar_table_ident(self):
    comando_sql = """create table ident_grafo
                     (id   integer primary key autoincrement,
                      dump integer);"""
    con = sql.connect(self.banco)
    con.execute(comando_sql)
    con.close()
    print("Criada tabela de identificação")
    
  def criar_tabela_grafos(self):
    comando_sql = """create table informacao_grafo
                     (id          integer   primary key not null,
                      num_pontos  integer   not null,
                      num_arestas integer   not null,
                      max_ponto   float not null);"""
    con = sql.connect(self.banco)
    con.execute(comando_sql)
    con.close()
    print("Tabela informacao_grafo criada")

  def criar_tabela_dijkstra(self):
    comando_sql = """create table informacao_dijkstra
                     (ponto_origem  integer          not null,
                      ponto_destino integer          not null,
                      caminho       varchar(max) not nulll,
                      num_passos    integer          not null,
                      tempo         float        not null,
                      id            integer          not null.
                      primary key(ponto_origem, ponto_destino)
                      foreign key(id) references informacao_grafo(id));"""
    con = sql.connect(self.banco)
    con.execute(comando_sql)
    con.close()
    print("Tabela informacao_dijkstra criada")

  def criar_tabela_astar(self):
    comando_sql = """create table informacao_astar
                     (ponto_origem  integer          not null,
                      ponto_destino integer          not null,
                      caminho       varchar(max) not nulll,
                      num_passos    integer          not null,
                      tempo         float        not null,
                      id            integer          not null.
                      primary key(ponto_origem, ponto_destino)
                      foreign key(id) references informacao_grafo(id));"""
    con = sql.connect(self.banco)
    con.execute(comando_sql)
    con.close()
    print("Tabela informacao_astar criada")

  def inserir_grafo(self,grafo):
    comando_sql = """insert into informacao_grafo(id,num_pontos,num_arestas,max_ponto)
                     values(?,?,?,?)"""
    con = sql.connect(self.banco)
    con.execute(comando_sql,(grafo.ident,len(grafo),grafo.num_arestas,grafo.max_x))
    con.commit()
    con.close()
    print("Grafo inserido corretamente")

  def inserir_tabela_dijkstra(self,dados):
    comando_sql = """insert into informacao_dijkstra(ponto_origem,ponto_destino,caminho,num_passos,tempo)
                     values(?,?,?,?,?)"""
    con = sql.connect(self.banco)
    con.execute(comando_sql,dados)
    con.commit()
    con.close()
    print("Dados de dijkstra inseridos corretamente")

  def inserir_tabela_astar(self,dados):
    comando_sql = """insert into informacao_astar(ponto_origem,ponto_destino,caminho,num_passos,tempo)
                     values(?,?,?,?,?)"""
    con = sql.connect(self.banco)
    con.execute(comando_sql,dados)
    con.commit()
    con.close()
    print("Dados de astar inseridos corretamente")

  def get_grafos(self):
    comando_sql = """select *
                       from informacao_grafo;"""
    con = sql.connect(self.banco)
    lista = self.get_lista_de_cursor(con.execute(comando_sql))  
    con.close()
    return lista

  def get_dijkstra(self):
    comando_sql = """select *
                       from informacao_dijkstra;"""
    con = sql.connect(self.banco)
    lista = self.get_lista_de_cursor(con.execute(comando_sql))
    con.close()
    return lista
      
  def get_astar(self):
    comando_sql = """select *
                       from informacao_astar;"""
    con = sql.connect(self.banco)
    lista = self.get_lista_de_cursor(con.execute(comando_sql))
    con.close()
    return lista

  def get_tempos_dijkstra(self):
    comando_sql = """select g.id, g.num_pontos, g.num_arestas, d.ponto_origem, d.ponto_destino, d.caminho, d.num_passos, d.tempo
                       from informacao_grafo g,
                            informacao_dijkstra d
                      where g.id = d.id;"""
    con = sql.connect(self.banco)
    lista = self.get_lista_de_cursor(con.execute(comando_sql))
    con.close()
    return lista

  def get_tempos_astar(self):
    comando_sql = """select g.id, g.num_pontos, g.num_arestas, a.ponto_origem, a.ponto_destino, a.caminho, a.num_passos, a.tempo
                       from informacao_grafo g,
                            informacao_astar a
                      where g.id = a.id;"""
    con = sql.connect(self.banco)
    lista = self.get_lista_de_cursor(con.execute(comando_sql))
    con.close()
    return lista
  
  def get_lista_de_cursor(self,cursor):
    lista = list()
    for elemento in cursor:
      lista.append(elemento)
    return lista
