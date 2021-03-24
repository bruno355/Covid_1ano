#Importação das Bilbiotecas
import pandas as pd
import numpy as np

#Leitura do dataset
file = 'drive/My Drive/covid_19_data.csv'

#Informando ao pandas que uma coluna que é data
df = pd.read_csv(file,sep=',',parse_dates=['ObservationDate'])

#Criação de uma nova variável
df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

#Corrigindo um erro na base de dados no nome da China
df['Country/Region'] = df['Country/Region'].replace('Mainland China', 'China')

#Renomeando as colunas para Português
df = df.rename(columns={'ObservationDate':'Data'})
df = df.rename(columns={'Province/State':'Provincia/Estados'})
df = df.rename(columns={'Country/Region':'País'})
df = df.rename(columns={'Last Update':'Data Atualizada'})
df = df.rename(columns={'Confirmed':'Confirmados'})
df = df.rename(columns={'Deaths': 'Mortos'})
df =df.rename(columns={'Recovered':'Recuperados'})
df = df.rename(columns={'Active':'Ativos'})

#Eliminando dados faltantes
df[['Provincia/Estados']] = df[['Provincia/Estados']].fillna('')
df[['Confirmado', 'Confirmado', 'Recuperados','Ativos']] = df[['Confirmado', 'Confirmado', 'Recuperados','Ativos']].fillna(0)

#Criando uma nova variável e agrupando dados para o melhor analise
df_agrupados = df.groupby(['Data','País'])['Confirmado', 'Mortos','Recuperados','Ativos'].sum().reset_index()

#Organizando as colunas
df_agrupados.sort_values(by='Confirmado', ascending=False)
