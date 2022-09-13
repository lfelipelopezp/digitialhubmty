# Databricks notebook source
# MAGIC %md
# MAGIC ##Leer CSVs desde Azure

# COMMAND ----------

import pandas as pd

# COMMAND ----------

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
df_Olimpicos = pd.read_csv(path)
display(df_Olimpicos)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Actividad: Competidores Olímpicos

# COMMAND ----------

#1- Cuál es el competidor más veterano que ha recibido medalla para los NOC´s MEX, COL y ARG (oro, plata o bronce) ?

df_ejercicio = df_Olimpicos

#Eliminar edad null
indexes = df_ejercicio[df_ejercicio['Age'].isnull()].index
df_ejercicio = df_ejercicio.drop(index = indexes, inplace= False, axis = 0)

#Eliminar medallas null
indexes = df_ejercicio[df_ejercicio['Medal'].isnull()].index
df_ejercicio = df_ejercicio.drop(index = indexes, inplace= False, axis = 0)

competidor_veterano = df_ejercicio

#Filtrar sólo MX, COL y ARG
competidor_veterano = competidor_veterano[competidor_veterano['NOC'].isin(['MEX', 'COL', 'ARG'])]
competidor_veterano_MEX = competidor_veterano[competidor_veterano['NOC'] == 'MEX']
competidor_veterano_ARG = competidor_veterano[competidor_veterano['NOC'] == 'ARG']
competidor_veterano_COL = competidor_veterano[competidor_veterano['NOC'] == 'COL']


#nombre_veterano = competidor_veterano[competidor_veterano['Age'] == max(competidor_veterano['Age'])]['Name'].item()
nombre_veterano_MEX = competidor_veterano_MEX[competidor_veterano_MEX['Age'] == max(competidor_veterano_MEX['Age'])]['Name']
nombre_veterano_MEX = nombre_veterano_MEX.head(1).item()

nombre_veterano_ARG = competidor_veterano_ARG[competidor_veterano_ARG['Age'] == max(competidor_veterano_ARG['Age'])]['Name']
nombre_veterano_ARG = nombre_veterano_ARG.head(1).item()

nombre_veterano_COL = competidor_veterano_COL[competidor_veterano_COL['Age'] == max(competidor_veterano_COL['Age'])]['Name']
nombre_veterano_COL = nombre_veterano_COL.head(1).item()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2 - Cuá es el competidor más joven que ha recibido medalla de oro para los NOC´s USA y CAN
competidor_joven = df_ejercicio
competidor_joven = competidor_joven[competidor_joven['Medal'] == 'Gold']

competidor_joven_USA = competidor_joven[competidor_joven['NOC'] == 'USA']
competidor_joven_CAN = competidor_joven[competidor_joven['NOC']== 'CAN']

nombre_joven_USA = competidor_joven_USA[competidor_joven_USA['Age'] == min(competidor_joven_USA['Age'])]['Name']
nombre_joven_USA = nombre_joven_USA.head(1).item()

nombre_joven_CAN = competidor_joven_CAN[competidor_joven_CAN['Age'] == min(competidor_joven_CAN['Age'])]['Name']
nombre_joven_CAN = nombre_joven_CAN.head(1).item()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3 - Encuentra al competidor más ganador de la historia en medallas totales, medallas de oro, medallas de plata y medallas de broce para los NOC´s USA, CHN y RUS. Crea un csv con toda su información.

competidor_ganador = df_ejercicio
competidor_ganador = competidor_ganador[competidor_ganador['NOC'].isin(['USA', 'CHN', 'RUS'])][['NOC','Name', 'Medal']]

competidor_ganador_USA = competidor_ganador[competidor_ganador['NOC'].isin(['USA'])][['NOC','Name', 'Medal']]
competidor_ganador_CHN = competidor_ganador[competidor_ganador['NOC'].isin(['CHN'])][['NOC','Name', 'Medal']]
competidor_ganador_RUS = competidor_ganador[competidor_ganador['NOC'].isin(['RUS'])][['NOC','Name', 'Medal']]

competidor_ganador_USA = competidor_ganador_USA.groupby(["NOC",'Name']).Medal.count().sort_values(ascending=False).head(3)
competidor_ganador_CHN = competidor_ganador_CHN.groupby(["NOC",'Name']).Medal.count().sort_values(ascending=False).head(3)
competidor_ganador_RUS = competidor_ganador_RUS.groupby(["NOC",'Name']).Medal.count().sort_values(ascending=False).head(3)


#CSVs
#competidor_ganador_USA.to_csv(path_res)
#competidor_ganador_CHN.to_csv(path_res)
#competidor_ganador_RUS.to_csv(path_res)




# COMMAND ----------

print(f"Los más veteranos con medalla en MEX, ARG y COL: {nombre_veterano_MEX}, {nombre_veterano_ARG} y {nombre_veterano_COL}.")
print(f'Los más jovenes con oro en USA y CAN: {nombre_joven_USA} y {nombre_joven_CAN}.')
print("\nLos deportistas con más medallas de la historia de USA son:\n",competidor_ganador_USA)
print("\nLos deportistas con más medallas de la historia de CHN son:\n",competidor_ganador_CHN)
print("\nLos deportistas con más medallas de la historia de RUS son:\n",competidor_ganador_RUS)
print("\nSe exportaron los datos en CSV.")

# COMMAND ----------

competidor_veterano["Medal"].unique()
