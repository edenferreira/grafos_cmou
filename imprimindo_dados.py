from banco_dados import *
                            
d = conexao().get_tempos_dijkstra_sem_caminho()
a =  conexao().get_tempos_astar_sem_caminho()

with open('dicionario_dados.txt','w') as arq:
  print('Tempos dos Algoritmos',file=arq)
  print('                    Dijkstra                 A*',file=arq)
with open('dicionario_dados.txt','a') as arq:
  for i in range(len(d['id'])):
    for key in d:
      print(key.rjust(15),' : ',str(d[key][i]).ljust(20),' : ', str(a[key][i]),file=arq)
