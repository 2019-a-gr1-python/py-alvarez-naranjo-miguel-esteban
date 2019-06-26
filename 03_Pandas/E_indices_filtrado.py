# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:15:13 2019

@author: MIGUELESTEBAN
"""

import pandas as pd

path_guardado = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/03_Pandas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

serie_artistas_duplicados = df_completo_pickle['artist']

artistas = pd.unique(serie_artistas_duplicados)

artistas.size

len(artistas)

blake = df_completo_pickle['artist'] == 'Blake, William'

type(blake)

blake.value_counts()

df_blake = df_completo_pickle[blake]

df_blake