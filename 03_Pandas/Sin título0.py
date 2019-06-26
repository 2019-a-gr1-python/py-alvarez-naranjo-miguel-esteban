# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:23:32 2019

@author: MIGUELESTEBAN
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/03_Pandas/data/csv/artwork_data.pickle'

df_completo_picke = pd.read_pickle(path_guardado)

df = df_completo_picke.iloc[49980:50019,:].copy()


# Tipos de archivos 

# - JSON
# - SQL
# - EXCEL


############################# EXCEL ############################
# se guarda en la carpeta del usuario
df.to_excel('ejemplo_basico.xlsx')
df.to_excel('ejemplo_basico_sin_indices.xlsx', index = False)