import pandas as pd
import numpy as np
from datetime import date

def le_planilha(planilha_dados, separador = ",", decimais = ",", encode='utf-8'):
  df_dados = pd.read_csv(planilha_dados, decimal=decimais, sep=separador, encoding=encode)
  return df_dados

def qtd_atendimentos_anteriores(cod_paciente, data_internacao, df_atendimentos):
  df_temp = df_atendimentos[df_atendimentos.CD_PACIENTE == cod_paciente]
  return df_temp[df_temp.DH_ATENDIMENTO_INT < data_internacao].count()[0]

def cria_planilha(dataframe, nome, caminho, separador=","):
  dataframe.to_csv(caminho + nome, sep=separador)

def converte_para_datetime(dataset, colunas, format = None):
  for coluna in colunas:
    dataset[coluna] = pd.to_datetime(dataset[coluna], dayfirst=True, errors='coerce',  format=format)