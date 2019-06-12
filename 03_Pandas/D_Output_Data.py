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
artistas_contados.to_excel(writer, sheet_name = 'Artistas Contados1')
artistas_contados.to_excel(writer, sheet_name = 'Artistas Contados2')
artistas_contados.to_excel(writer, sheet_name = 'Artistas Contados3')
artistas_contados.to_excel(writer, sheet_name = 'Artistas Contados4')

hoja_artistas = writer.sheets['Artistas Contados']
hoja_artistas1 = writer.sheets['Artistas Contados1']
hoja_artistas2 = writer.sheets['Artistas Contados2']
hoja_artistas3 = writer.sheets['Artistas Contados3']
hoja_artistas4 = writer.sheets['Artistas Contados4']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': '2_color_scale', 
        'min_value': '10', 
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'}

hoja_artistas.conditional_format(rango_celdas, formato)

hoja_artistas1.conditional_format(rango_celdas, {'type': 'data_bar'})

hoja_artistas2.conditional_format(rango_celdas, {'type': 'icon_set',
     'icon_style': '4_red_to_black',
     'icons': [{'criteria': '>=', 'type': 'number',     'value': 90},
               {'criteria': '<',  'type': 'percentile', 'value': 50},
               {'criteria': '<=', 'type': 'percent',    'value': 25}]})

hoja_artistas3.conditional_format(rango_celdas, {'type': 'icon_set',
                                       'icon_style': '3_traffic_lights',
                                       'icons': [{'criteria': '>=', 'type': 'number',     'value': 90},
               {'criteria': '<',  'type': 'percentile', 'value': 50},
               {'criteria': '<=', 'type': 'percent',    'value': 25}]})

writer.save()



########################## SQL ########################



with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('Alguien', conexion)


## with mysql.connect('mysql://user:password@ip:puerto.db') as conexion:
##     df.to_sql('Alguien', conexion)
    
## with sqlite3.connect('bdd_python.db') as conexion:
##     df.to_sql('Alguien', conexion)





############################ JSON #########################3

df.to_json('artistas.json')
df.to_json('artistas_orientado_tabla.json', orient = 'table')





































