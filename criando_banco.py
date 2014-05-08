from banco_dados import *

con = conexao()
con.criar_table_ident()
con.criar_tabela_grafos()
con.criar_tabela_dijkstra()
con.criar_tabela_astar()
