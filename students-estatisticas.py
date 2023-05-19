# ALUNOS:
## Francisco Racklyn Sotero dos Santos - 21110615
## Lucas Barbosa Leite Silva - 21110616

import pandas as pd

# importando dataset
df = pd.read_csv('./StudentsPerformance.csv')

# Filtrando linhas e criando dataframes separados por gênero
male_df = df.query('gender == "male"')
female_df = df.query('gender == "female"')

# A - Cálculo da média em matemática (math score) de ambos os gêneros
print("A - MÉDIA EM MATEMÁTICA:")
print("--Masculino: ", male_df['math score'].mean())
print("--Feminino: ", female_df['math score'].mean())

# B - Cálculo do desvio padrão em matemática (math score) de ambos os gêneros
print("\nB - DESVIO PADRÃO EM MATEMÁTICA:")
print("--Masculino: ", male_df['math score'].std())
print("--Feminino: ", female_df['math score'].std())

# C - Tamanho da amostra em matemática (math score) de ambos os gêneros
print("\nC - TAMANHO DA AMOSTRA EM MATEMÁTICA:")
print("--Masculino: ", male_df['math score'].count())
print("--Feminino: ", female_df['math score'].count())

# D - Cálculo da média em escrita (writing score) de ambos os gêneros
print("\nD - MÉDIA EM ESCRITA:")
print("--Masculino: ", male_df['writing score'].mean())
print("--Feminino: ", female_df['writing score'].mean())

# E - Cálculo do desvio padrão em escrita (writing score) de ambos os gêneros
print("\nE - DESVIO PADRÃO EM ESCRITA:")
print("--Masculino: ", male_df['writing score'].std())
print("--Feminino: ", female_df['writing score'].std())

# F - Tamanho da amostra em escrita (writing score) de ambos os gêneros
print("\nF - TAMANHO DA AMOSTRA EM ESCRITA:")
print("--Masculino: ", male_df['writing score'].count())
print("--Feminino: ", female_df['writing score'].count())

# G - Cálculo da média em leitura (reading score) de ambos os gêneros
print("\nG - MÉDIA EM LEITURA:")
print("--Masculino: ", male_df['reading score'].mean())
print("--Feminino: ", female_df['reading score'].mean())

# H - Cálculo do desvio padrão em leitura (reading score) de ambos os gêneros
print("\nH - DESVIO PADRÃO EM LEITURA:")
print("--Masculino: ", male_df['reading score'].std())
print("--Feminino: ", female_df['reading score'].std())

# I - Tamanho da amostra em leitura (reading score) de ambos os gêneros
print("\nI - TAMANHO DA AMOSTRA EM LEITURA:")
print("--Masculino: ", male_df['reading score'].count())
print("--Feminino: ", female_df['reading score'].count())