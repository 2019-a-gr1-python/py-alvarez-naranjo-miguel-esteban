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

columnas = ['artist', 'title', 'year']
df.to_excel('columnas.xlsx', columns = columnas)

# Multiples hojas de trabajos (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx', engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')
df.to_excel(writer, sheet_name = 'Preview Dos', index = False)
df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()

# Formateo Condicional

artistas_contados = df_completo_picke['artist'].value_counts()
writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')
artistas_contados.to_excel(writer, sheet_name = 'Artistas Contados')

hoja_artistas = writer.sheets['Artistas Contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': '2_color_scale', 
        'min_value': '10', 
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'}

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()



########################## SQL ########################


















































