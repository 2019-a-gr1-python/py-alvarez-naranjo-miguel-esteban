# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:09:48 2019

@author: MIGUELESTEBAN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

# URL donde se obtuvieron los datos: https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Current-Year-To-Date-/5uac-w243



path_CSV = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/Proyecto 1er Bim/Data/NYPD_Complaint_Data_Current__Year_To_Date_.csv'
path_mapa = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/Proyecto 1er Bim/Data/citymap_citymap_v1/citymap_citymap_v1.shp'

columnas_a_usar = ['CMPLNT_NUM','ADDR_PCT_CD','BORO_NM',
                   'CMPLNT_FR_DT','CMPLNT_FR_TM','CMPLNT_TO_DT',
                   'CMPLNT_TO_TM','CRM_ATPT_CPTD_CD','HADEVELOPT',
                   'HOUSING_PSA','JURISDICTION_CODE','JURIS_DESC',
                   'KY_CD','LAW_CAT_CD','LOC_OF_OCCUR_DESC',
                   'OFNS_DESC','PARKS_NM','PATROL_BORO',
                   'PD_CD','PD_DESC','PREM_TYP_DESC',
                   'RPT_DT','STATION_NAME','SUSP_AGE_GROUP',
                   'SUSP_RACE','SUSP_SEX','TRANSIT_DISTRICT',
                   'VIC_AGE_GROUP','VIC_RACE','VIC_SEX',
                   'X_COORD_CD','Y_COORD_CD','Latitude',
                   'Longitude','Lat_Lon']


df_completo = pd.read_csv(
        path_CSV,
        usecols = columnas_a_usar,
        parse_dates = True,
        index_col = 'CMPLNT_NUM')



df_completo.fillna(0)
# graficar el mapa
NY_street_map = gpd.read_file(path_mapa)
fig,ax = plt.subplots(figsize = (15,15))
NY_street_map.plot(ax = ax)

geometry = [Point(xy) for xy in zip(df_completo['latitude'], df_completo['longitude'])]
geometry[:3]


df_barrios_NY = pd.unique(df_completo['BORO_NM'])

for x in df_barrios_NY:
    print(x)  


df_seccion_barrios = df_completo['BORO_NM']


# filtrado por barrio y creacion de data frames

QUEENS = df_completo['BORO_NM'] == 'QUEENS'

df_QUEENS = df_completo[QUEENS]

BRONX = df_completo['BORO_NM'] == 'BRONX'

df_BRONX = df_completo[BRONX]

MANHATTAN = df_completo['BORO_NM'] == 'MANHATTAN'

df_MANHATTAN = df_completo[MANHATTAN]

BROOKLYN = df_completo['BORO_NM'] == 'BROOKLYN'

df_BROOKLYN = df_completo[BROOKLYN]

STATEN_ISLAND = df_completo['BORO_NM'] == 'STATEN ISLAND'

df_STATEN_ISLAND = df_completo[STATEN_ISLAND]

BarrioDesconocido = df_completo['BORO_NM'] == ''

df_BarrioDesconocido = df_completo[BarrioDesconocido]



# cambiar a formato fecha

df_QUEENS['CMPLNT_FR_DT'] = pd.to_datetime(df_QUEENS.CMPLNT_FR_DT)

df_QUEENS.count()
len(df_QUEENS)
