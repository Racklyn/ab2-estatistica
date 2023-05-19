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

# Função para calcular limite superior do Intervalo de Confiança dos dados
def calcularICMax(data):
    alfa = 0.05 # Probabilidade de erro (95% de confiança)
    z = st.norm.pdf(1 - alfa/2) # Encontrando valor do z-index

    mean = data.mean() # média dos valores
    std = data.std() # desvio padrão dos valores
    n = data.count() # quantidade de valores

    sup = mean + z * std/np.sqrt(n) # cálculo do limite superior do IC

    return sup


def testeHip(data, value_to_compare):

    ## Formulando hipótese:
    H0 = value_to_compare
    #H0 <= ICmax
    #H1 > ICmax

    ## Nível de significância
    alfa = 0.05
    n = data.count()

    media_am = data.mean()
    s = data.std() # ddof=1?

    ## Estatística de teste Z
    z = (media_am - H0) / (s / np.sqrt(n))

    ## Região crítica:
    z_critico = st.norm.pdf(1 - alfa) # TODO: Verificar isso


    # Queremos verificar a Hip alternativa (H1)???? VERIFICAR ISSO

    if z > z_critico:
        # Rejeita hip nula (H0), e não rejeita H1
        print("NÃO Rejeita")
    else:
        # Rejeita hip alternativa (H1), e não rejeita H0
        print("Rejeita")
    



print("A - Hip. média matemática masculino > IC_sup média matemática feminino")
testeHip(male_df['math score'], calcularICMax(female_df['math score']))