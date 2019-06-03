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
        parse_dates = ['CMPLNT_FR_DT', 'CMPLNT_TO_DT', 'RPT_DT'],
        )



#df_completo.fillna(0)

df_completo = df_completo[df_completo.CMPLNT_NUM != 418784447]
df_completo = df_completo[df_completo.CMPLNT_NUM != 160867902]
df_completo = df_completo[df_completo.CMPLNT_NUM != 691037884]
df_completo = df_completo[df_completo.CMPLNT_NUM != 186099981]
df_completo = df_completo[df_completo.CMPLNT_NUM != 794492299]
df_completo = df_completo[df_completo.CMPLNT_NUM != 813648479]
df_completo = df_completo[df_completo.CMPLNT_NUM != 870176415]
df_completo = df_completo[df_completo.CMPLNT_NUM != 386936950]
df_completo = df_completo[df_completo.CMPLNT_NUM != 837889016]
df_completo = df_completo[df_completo.CMPLNT_NUM != 291498531]
df_completo = df_completo[df_completo.CMPLNT_NUM != 469624613]
df_completo = df_completo[df_completo.CMPLNT_NUM != 335349746]
df_completo = df_completo[df_completo.CMPLNT_NUM != 168683913]
df_completo = df_completo[df_completo.CMPLNT_NUM != 361877450]
df_completo = df_completo[df_completo.CMPLNT_NUM != 380335489]
df_completo = df_completo[df_completo.CMPLNT_NUM != 677785742]

path_guardado = 'C:/Users/MIGUELESTEBAN/Documents/GitHub/py-alvarez-naranjo-miguel-esteban/Proyecto 1er Bim/Data/NYPD_Complaint_Data_Current__Year_To_Date_.pickle'

df_completo.to_pickle(path_guardado)


df = pd.read_pickle(path_guardado)
# tipar la fecha con tipo date
df['CMPLNT_FR_DT'] = pd.to_datetime(df.CMPLNT_FR_DT)


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

QUEENS = df['BORO_NM'] == 'QUEENS'

df_QUEENS = df[QUEENS]

BRONX = df['BORO_NM'] == 'BRONX'

df_BRONX = df[BRONX]

MANHATTAN = df['BORO_NM'] == 'MANHATTAN'

df_MANHATTAN = df[MANHATTAN]

BROOKLYN = df['BORO_NM'] == 'BROOKLYN'

df_BROOKLYN = df[BROOKLYN]

STATEN_ISLAND = df['BORO_NM'] == 'STATEN ISLAND'

df_STATEN_ISLAND = df[STATEN_ISLAND]

BarrioDesconocido = df['BORO_NM'] == ''

df_BarrioDesconocido = df[BarrioDesconocido]

df.count()

# filtrar barrios por fechas desde 2016 hasta mediados de 2019


df_QUEENS2019 = df_QUEENS.loc[df_QUEENS.CMPLNT_FR_DT >= '2019-01-01']
mask1 = (df_QUEENS['CMPLNT_FR_DT'] > '2017-12-31') & (df_QUEENS['CMPLNT_FR_DT'] <= '2018-12-31')
df_QUEENS2018 = df_QUEENS.loc[mask1]

mask2 = (df_QUEENS['CMPLNT_FR_DT'] > '2016-12-31') & (df_QUEENS['CMPLNT_FR_DT'] <= '2017-12-31')
df_QUEENS2017 = df_QUEENS.loc[mask2]

mask3 = (df_QUEENS['CMPLNT_FR_DT'] > '2015-12-31') & (df_QUEENS['CMPLNT_FR_DT'] <= '2016-12-31')
df_QUEENS2016 = df_QUEENS.loc[mask3]

df_BRONX2019 = df_BRONX.loc[df_BRONX.CMPLNT_FR_DT >= '2019-01-01']
mask4 = (df_BRONX['CMPLNT_FR_DT'] > '2017-12-31') & (df_BRONX['CMPLNT_FR_DT'] <= '2018-12-31')
df_BRONX2018 = df_BRONX.loc[mask4]

mask5 = (df_BRONX['CMPLNT_FR_DT'] > '2016-12-31') & (df_BRONX['CMPLNT_FR_DT'] <= '2017-12-31')
df_BRONX2017 = df_BRONX.loc[mask5]

mask6 = (df_BRONX['CMPLNT_FR_DT'] > '2015-12-31') & (df_BRONX['CMPLNT_FR_DT'] <= '2016-12-31')
df_BRONX2016 = df_BRONX.loc[mask6]

df_MANHATTAN2019 = df_MANHATTAN.loc[df_MANHATTAN.CMPLNT_FR_DT >= '2019-01-01']
mask7 = (df_MANHATTAN['CMPLNT_FR_DT'] > '2017-12-31') & (df_MANHATTAN['CMPLNT_FR_DT'] <= '2018-12-31')
df_MANHATTAN2018 = df_MANHATTAN.loc[mask7]

mask8 = (df_MANHATTAN['CMPLNT_FR_DT'] > '2016-12-31') & (df_MANHATTAN['CMPLNT_FR_DT'] <= '2017-12-31')
df_MANHATTAN2017 = df_MANHATTAN.loc[mask8]

mask9 = (df_MANHATTAN['CMPLNT_FR_DT'] > '2015-12-31') & (df_MANHATTAN['CMPLNT_FR_DT'] <= '2016-12-31')
df_MANHATTAN2016 = df_MANHATTAN.loc[mask9]

df_BROOKLYN2019 = df_BROOKLYN.loc[df_BROOKLYN.CMPLNT_FR_DT >= '2019-01-01']
mask16 = (df_BROOKLYN['CMPLNT_FR_DT'] > '2017-12-31') & (df_BROOKLYN['CMPLNT_FR_DT'] <= '2018-12-31')
df_BROOKLYN2018 = df_BROOKLYN.loc[mask16]

mask17 = (df_BROOKLYN['CMPLNT_FR_DT'] > '2016-12-31') & (df_BROOKLYN['CMPLNT_FR_DT'] <= '2017-12-31')
df_BROOKLYN2017 = df_BROOKLYN.loc[mask17]

mask18 = (df_BROOKLYN['CMPLNT_FR_DT'] > '2015-12-31') & (df_BROOKLYN['CMPLNT_FR_DT'] <= '2016-12-31')
df_BROOKLYN2016 = df_BROOKLYN.loc[mask18]

df_STATEN_ISLAND2019 = df_STATEN_ISLAND.loc[df_STATEN_ISLAND.CMPLNT_FR_DT >= '2019-01-01']
mask16 = (df_STATEN_ISLAND['CMPLNT_FR_DT'] > '2017-12-31') & (df_STATEN_ISLAND['CMPLNT_FR_DT'] <= '2018-12-31')
df_STATEN_ISLAND2018 = df_STATEN_ISLAND.loc[mask16]

mask17 = (df_STATEN_ISLAND['CMPLNT_FR_DT'] > '2016-12-31') & (df_STATEN_ISLAND['CMPLNT_FR_DT'] <= '2017-12-31')
df_STATEN_ISLAND2017 = df_STATEN_ISLAND.loc[mask17]

mask18 = (df_STATEN_ISLAND['CMPLNT_FR_DT'] > '2015-12-31') & (df_STATEN_ISLAND['CMPLNT_FR_DT'] <= '2016-12-31')
df_STATEN_ISLAND2016 = df_STATEN_ISLAND.loc[mask18]






seccion_df = df_QUEENS2019.copy()

df_agrupado_ay = seccion_df.groupby('OFNS_DESC')
for OFNSDESC, registros in df_agrupado_ay:
    print(OFNSDESC)
    

ofensas = pd.unique(df_QUEENS2019['OFNS_DESC'])
cantidadOfensas = df_QUEENS2019.copy().groupby('OFNS_DESC')
df_cantidadOfensas = pd.DataFrame(cantidadOfensas['CMPLNT_NUM'].count())

df_cantidadOfensas.plot(kind='bar')#grafico de ofensas vs cantidad de ofensas


arregloOfensas = df_cantidadOfensas['CMPLNT_NUM']




cantidad_genero = df_QUEENS2019.copy().groupby('SUSP_SEX')
df_cantidad_genero = pd.DataFrame(cantidad_genero['SUSP_SEX'].count())
df_cantidad_genero.plot(kind='bar', color='green')







df_QUEENS.count()
len(df_QUEENS)



