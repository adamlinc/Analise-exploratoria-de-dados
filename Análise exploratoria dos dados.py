# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:55:12 2019

@author: ADAMLINCOLNOLIVEIRAS
"""

import pandas as pd


#importando o arquivo para dentro de um data frame chamado DATA
#NEsse ponto aprendi que eu posso passar o caminho completo do arquivo utilizando contra barras duplas no lugar das simples. =)

data_bol = pd.read_csv('C:\\Users\\ADAMLINCOLNOLIVEIRAS\\Desktop\\Dados de Acidentes BH\\BOL - Boletim de Ocorrencia\\bol_consolidado.csv', sep=';', encoding='utf-8')
data_env = pd.read_csv('C:\\Users\\ADAMLINCOLNOLIVEIRAS\\Desktop\\Dados de Acidentes BH\\ENV - Acidentes de transito com vitima dados gerais\\ENV_consolidado.csv', sep=';', encoding='utf-8')
data_log = pd.read_csv('C:\\Users\\ADAMLINCOLNOLIVEIRAS\\Desktop\\Dados de Acidentes BH\\LOG - Local do Acidente\\LOG_consolidado.csv', sep=';', encoding='utf-8')
data_veic = pd.read_csv('C:\\Users\\ADAMLINCOLNOLIVEIRAS\\Desktop\\Dados de Acidentes BH\\VEIC - Dados dos Veiculos\\VEIC_consolidado.csv', sep=';', encoding='utf-8')

#excluindo algumas colunas que não são de interesse
#data.drop(['Unnamed: 0','Photo','Flag','Club Logo'], axis = 1, inplace = True)

#Utilo o Dtype para verificar o tipo dos registros.
data.dtypes

#Quantidade de linhas e colunas do DataFrame
>>> data.shape

#Descrição do Index
>>> data.index

#Colunas presentes no DataFrame
>>> data.columns

#Contagem de dados não-nulos, aqui eu posso ver se existem celulas em branco caso o numero de dados não seja igual ao numero de linhas para cada uma das colunas.
>>> data.count()

#Aplicando uma função que substitui a por b
#data.apply(lambda x: x.replace('a', 'b'))

#Conta quantas linhas tem na coluna 1
data_bol.count(1)


#Selecionando a primeira linha da coluna data hora para verificar como essa data hora esta vindo.
data.loc[0, 'data hora_boletim']

#alterar tipo de dados
#data.data hora_boletim.astype(int)


#criando um novo campo no data frame que diz se a linha é duplicada, ela retorna TRUE or FALSE
data_bol["is_duplicate"]= data_bol.duplicated()

#utilizando metodo filter para verificar se tem algum numero de duplicado caso a coluna duplicate seja TRUE.
data_bol = data_bol.filter(like='true', axis=0)
print (data_bol)



