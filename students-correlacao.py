# ALUNOS:
## Francisco Racklyn Sotero dos Santos - 21110615
## Lucas Barbosa Leite Silva - 21110616

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('StudentsPerformance.csv')

matematica = dados['math score']
escrita = dados['writing score']
leitura = dados['reading score']

def calculaClasseCorrelacao(r):
    if(r>=0 and r<=0.1):
        print("A correlação é muito baixa. r:",r)
    elif(r>0.1 and r<=0.3):
        print("A correlação é baixa. r:",r)
    elif(r>0.3 and r<=0.5):
        print("A correlação é moderada. r:",r)
    elif(r>0.5 and r<=0.7):
        print("A correlação é alta. r:",r)
    elif(r>0.7 and r<=0.9):
        print("A correlação é muito alta. r:",r)
    elif(r>0.9):
        print("A correlação é quase perfeita. r:",r)

print("A: Analisando a correlação entre as notas de Matemática e Escrita:")
print("Gráfico de Dispersão:")
plt.scatter(matematica, escrita)
plt.title("Gráfico de Dispersão")
plt.xlabel("Matemática")
plt.ylabel("Escrita")
plt.show()

print("Resultado da análise:")
r = np.corrcoef(matematica, escrita)[0, 1]
calculaClasseCorrelacao(r)

print("B: Analisando a correlação entre as notas de Matemática e Leitura:")
print("Gráfico de Dispersão:")
plt.scatter(matematica, leitura)
plt.title("Gráfico de Dispersão")
plt.xlabel("Matemática")
plt.ylabel("Leitura")
plt.show()

print("Resultado da análise:")
r = np.corrcoef(matematica, leitura)[0, 1]
calculaClasseCorrelacao(r)

print("C: Analisando a correlação entre as notas de Leitura e Escrita:")
print("Gráfico de Dispersão:")
plt.scatter(leitura, escrita)
plt.title("Gráfico de Dispersão")
plt.xlabel("Leitura")
plt.ylabel("Escrita")
plt.show()

print("Resultado da análise:")
r = np.corrcoef(leitura, escrita)[0, 1]
calculaClasseCorrelacao(r)