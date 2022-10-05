# Databricks notebook source
# MAGIC %md
# MAGIC ### Importar CSV alumnos

# COMMAND ----------

import pandas as pd
import seaborn as sb

path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Modulo 17 - Alumnos por grado/clean_students_complete.csv'
df_alumnos = pd.read_csv(path)
display(df_alumnos)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Ejercicio puntaje Reading 2

# COMMAND ----------

#Crea / Presenta la forma que creas más conveniente para describir qué grado por escuela tuvo el mejor puntaje en "reading" y con ello saber que genero es el que predomina en este filtro.

#Seleccionar columnas
df_EscuelaPuntajeReading = df_alumnos[['school_name','grade','reading_score', 'gender']]

df_EscuelaPuntajeReading_max = df_EscuelaPuntajeReading[df_EscuelaPuntajeReading['reading_score'] == df_EscuelaPuntajeReading['reading_score'].max()] #subdf mayor calif

print('Mix Género vs. MAX reading_score por grado:')
print(df_EscuelaPuntajeReading_max[['school_name', 'grade', 'reading_score' ,'gender']].value_counts().sort_values(ascending = True).head(10))



# COMMAND ----------

# MAGIC %md
# MAGIC ##Actividad: Gráfica por Categoria

# COMMAND ----------

#Crea / Presenta un algoritmo que genere los datos de "reading_score" y "math_score", en variables categóricas, y guárdalo en dos columnas diferentes (cada columna nueva representa la nueva columna con variables categórica). 

#Crea / Presenta una gráfica que condense la información obtenida ahora categóricamente mostrando que género obtuvo mejor puntaje.

def categoricas(x):
    if x < 60:
        return "Reprobado"
    elif x<75:
        return "Panzazo"
    else:
        return "Excelente"

df_calis = df_alumnos

df_calis["categoricas_reading_score"] = df_calis["reading_score"].apply(categoricas)
df_calis["categoricas_math_score"] = df_calis["math_score"].apply(categoricas)

display(df_calis)

# COMMAND ----------

grafica_calis = df_calis.groupby(["gender","categoricas_reading_score","categoricas_math_score"]).agg({"student_name":"count"}).reset_index()

sb.barplot(data=grafica_calis, x="categoricas_reading_score", y="student_name", hue="gender", palette = 'Spectral')
