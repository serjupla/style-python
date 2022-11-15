from fila_normal import fila_normal
from fila_prioritaria import FilaPrioritaria

# fila_teste = fila_normal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chama_cliente(12))
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(8))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(5))
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.estatisticas("10/01/2020",198,"detail"))