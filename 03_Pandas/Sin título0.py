# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 05:31:45 2019

@author: MIGUELESTEBAN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_delitosEC = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/Proyecto 2do Bim/scrapyDelitosEC/delitosEC.json'
df = pd.read_json(path_delitosEC)
df.rename(columns = {'DELITO:':'DELITO'}, inplace = True) 
# dividir la fecha en anios, mes y dia
df1 = df['FECHA'].apply(lambda x: pd.Series(x.split('-')))
df1.rename(columns = {0:'ANIO', 1:'MES', 2:'DIA'}, inplace = True) 
# dividir la columna lugar en provincia y canton
df2 = df['LUGAR'].apply(lambda x: pd.Series(x.split('-')))
df2.rename(columns = {0:'PROVINCIA', 1:'CANTON'}, inplace = True)
# dividir la hora en horas minutos y segundos
df3 = df['HORA'].apply(lambda x: pd.Series(x.split(':')))
df3.rename(columns = {0:'HORA', 1:'MINUTOS', 2:'SEGUNDOS'}, inplace = True) 
# unimos los dataframes

df_unido = pd.merge(df, df1, left_index=True, right_index=True)
df_unido2 = pd.merge(df_unido, df2, left_index=True, right_index=True)
df_completo = pd.merge(df_unido2, df3, left_index=True, right_index=True)
df_completo

cantidadOfensas = df_completo.copy().groupby('PROVINCIA')

df_cantidadOfensas = pd.DataFrame(cantidadOfensas.count()).sort_values('PROVINCIA')