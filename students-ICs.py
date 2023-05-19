# ALUNOS:
## Francisco Racklyn Sotero dos Santos - 21110615
## Lucas Barbosa Leite Silva - 21110616

import pandas as pd
import scipy.stats as st
import numpy as np

# importando dataset
df = pd.read_csv('./StudentsPerformance.csv')

# Filtrando linhas e criando dataframes separados por gênero
male_df = df.query('gender == "male"')
female_df = df.query('gender == "female"')

alfa = 0.05 # Probabilidade de erro (95% de confiança)
z = st.norm.pdf(1 - alfa/2) # Encontrando valor do z-index

# Função para calcular e exibir Intervalo de Confiança dos dados
def calcularIC(data):
    mean = data.mean() # média dos valores
    std = data.std() # desvio padrão dos valores
    n = data.count() # quantidade de valores

    sup = mean + z * std/np.sqrt(n) # cálculo do limite superior do IC
    inf = mean - z * std/np.sqrt(n) # cálculo do limite inferior do IC

    print(f'[{inf} - {sup}]\n')


# A - IC para média em matemática - masculino
print("A - IC média MATEMÁTICA masculino")
calcularIC(male_df['math score'])

# B - IC para média em matemática - feminino
print("B - IC média MATEMÁTICA feminino")
calcularIC(female_df['math score'])

# C - IC para média em leitura - masculino
print("C - IC média LEITURA masculino")
calcularIC(male_df['reading score'])

# D - IC para média em leitura - feminino
print("D - IC média LEITURA feminino")
calcularIC(female_df['reading score'])

# E - IC para média em escrita - masculino
print("E - IC média ESCRITA masculino")
calcularIC(male_df['writing score'])

# F - IC para média em escrita - feminino
print("F - IC IC média ESCRITA feminino")
calcularIC(female_df['writing score'])
