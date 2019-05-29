# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:16:32 2019

@author: MIGUELESTEBAN
"""

import json
import pandas as pd
import os

path = '/Users/carlosaguirre/Documents/GitHub/py-Aguirre-Maldonado-Carlos-Arturo/03_Pandas/data/artwork'

archivo = '/a/000/a00001-1035.json'

path_archivo = path + archivo

llaves = ['id','all_artists',
          'title','medium',
          'dateText','acquisitionYear',
          'height','width','units']

with open(path_archivo) as texto_json:
    contenido_json = json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)
    
    registro_df_lista = []
    for llave  in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    registro_df_tupla = tuple(registro_df)

print(registro_df_tupla)

df_chiquito = pd.DataFrame([registro_df_lista])
df_chiquito_t=pd.DataFrame([registro_df_tupla])

def leer_json(path,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista = []
    for llave  in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

leer_json(path_archivo,llaves)