# Databricks notebook source
# MAGIC %md
# MAGIC ##Graficas

# COMMAND ----------

import pandas as pd

# COMMAND ----------

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
df_Olimpicos = pd.read_csv(path)
#display(df_Olimpicos)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Actividad Grafica Medallas

# COMMAND ----------

#Crea una gráfica de barras que represente a los 10 países con más medallas ganadas en orden de menor a mayor y que muestre los valores de cada barra.
#Eliminar medallas null
indexes = df_Olimpicos[df_Olimpicos['Medal'].isnull()].index
df_Olimpicos = df_Olimpicos.drop(index = indexes, inplace= False, axis = 0)


#Obtener df con top 10 paises y medallas
df_medallas_pais_TOP10 = df_Olimpicos['NOC'].value_counts().head(10)
display(df_medallas_pais_TOP10)


paises_medalleros = df_Olimpicos[['NOC','Medal']]
paises_medalleros['NOC'].value_counts().head(10).plot(kind = 'bar', figsize = (12,5))



#Utilizar ".hist()"
