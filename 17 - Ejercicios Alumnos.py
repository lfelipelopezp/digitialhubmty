# Databricks notebook source
# MAGIC %md
# MAGIC ### Importar CSV alumnos

# COMMAND ----------

import pandas as pd

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
df_alumnos = pd.read_csv(path)
display(df_alumnos)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Ejercicio: Alumnos por grado

# COMMAND ----------

print(df_alumnos['grade'].value_counts().sort_values(ascending = True))
df_alumnos['grade'].value_counts().sort_values(ascending = True).plot(kind = 'bar', figsize = (12,5), )


# COMMAND ----------

# MAGIC %md
# MAGIC ##Ejercicio puntaje Reading

# COMMAND ----------

#Seleccionar columnas
df_EscuelaPuntajeReading = df_alumnos[['school_name', 'reading_score', 'gender']]

df_EscuelaPuntajeReading_max = df_EscuelaPuntajeReading[df_EscuelaPuntajeReading['reading_score'] == df_EscuelaPuntajeReading['reading_score'].max()] #subdf mayor calif
df_EscuelaPuntajeReading_min = df_EscuelaPuntajeReading[df_EscuelaPuntajeReading['reading_score'] == df_EscuelaPuntajeReading['reading_score'].min()] #subdf menor calif

print('Mix Género vs. MAX reading_score:')
print(df_EscuelaPuntajeReading_max[['school_name', 'gender']].value_counts().sort_values(ascending = True).head(10))
print('\nMix Género vs. MIN reading_score:')
print(df_EscuelaPuntajeReading_min[['school_name', 'gender']].value_counts().sort_values(ascending = True).head(10))
#df_EscuelaPuntajeReading_max['gender'].value_counts().sort_values(ascending = True).plot(kind = 'pie')


# COMMAND ----------

#print('\nMix Género vs. MIN reading_score:')
#print(df_EscuelaPuntajeReading_min['gender'].value_counts().sort_values(ascending = True))
#df_EscuelaPuntajeReading_min['gender'].value_counts().sort_values(ascending = True).plot(kind = 'pie')
