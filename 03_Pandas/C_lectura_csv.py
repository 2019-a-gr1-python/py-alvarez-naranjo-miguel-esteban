# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:18:23 2019

@author: dr
"""

import pandas as pd
import os

# Archivos texto -> JSON, CSV, HTML, XML....
# Binary Files -> (asasadasadasasa)
# Relational Databases

path = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/03_Pandas/data/csv/artwork_data.csv'

df = pd.read_csv(
        path,
        nrows = 5,
        usecols=['id','artist'],
        index_cols='id'
        )

columnas_a_usar = ['id', 'artist','title',
                   'medium','year','acquisitionYear',
                   'height','width','units'
                   ]



df_completo = pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col = 'id'
        )

path_guardado = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/03_Pandas/data/csv/artwork_data.pickle'

df_completo.to_pickle(path_guardado)

df_completo_pickel = pd.read_pickle(path_guardado)

df_completo.shape






















