# Databricks notebook source
# MAGIC %md
# MAGIC ##Leer CSVs desde Azure

# COMMAND ----------

import pandas as pd

# COMMAND ----------

#Leer de azure usando pyspark
path = 'dbfs:/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 12 - Actividad Competidores Olimpicos/athlete_events.csv'
data = (spark.read.option("header", True).option("inferSchema", True,).option("encoding", "utf-8").csv(path))
display(data)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Convertir a df de pandas

# COMMAND ----------

#Convertir a df de pandas
data_pandas = data.toPandas()
display(data_pandas)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Actividad: Competidores Olímpicos

# COMMAND ----------

#1- Cuál es el competidor más veterano que ha recibido medalla (oro, plata o bronce)?

#Crear copia de DF eliminando NAs en edad
competidor_veterano = data_pandas
indexes = competidor_veterano[competidor_veterano['Age'] == "NA"].index
competidor_veterano = competidor_veterano.drop(index = indexes, inplace= False, axis = 0)
#display(competidor_veterano)

nombre = competidor_veterano[competidor_veterano['Age'] == max(competidor_veterano['Age'])]
display(nombre)


#2 - Cuál es el competidor más joven que ha recibido medalla de oro?

#Encuentra al competidor más ganador de la historia en medallas totales, medallas de oro, medallas de plata y medallas de broce. 


#Crea un csv con toda su información.

# COMMAND ----------

competidor_veterano["Medal"].unique()
