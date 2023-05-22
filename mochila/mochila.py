# Algoritmo baseado em: https://www.youtube.com/watch?v=fC4mDO3RGQ8 - video explicativo:  Implementação de Algoritmo Genético - Problema da mochila - Python

from algoritmo import *
                   # Ítem [peso, valor]
pesos_e_valores = [[3, 266], [13, 442], [10, 671], [9, 526], \
                   [7, 388], [1, 245], [8, 210], [8, 145], \
                   [2, 126], [9, 332]]
peso_maximo = 100
n_de_cromossomos = 150
geracoes = 80
n_de_itens = len(pesos_e_valores) #Análogo aos pesos e valores

# Execução dos procedimentos
populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]
for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

# Prints do terminal
for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de valor na mochila: ", dados)

print("\nPeso máximo:",peso_maximo,"g\n\nItens disponíveis:")
for indice,i in enumerate(pesos_e_valores):
    print("Item ",indice+1,": ",i[0],"g | R$",i[1])
    
print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao[i])

# Gerador de gráfico
import matplotlib.pyplot as plt
# De matplotlib importar pyplot como plt
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da Mochila")
plt.xlabel("Geração")
plt.ylabel("Valor Médio da Mochila")
plt.show()