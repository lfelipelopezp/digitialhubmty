# Databricks notebook source
# MAGIC %md
# MAGIC ### Salarios

# COMMAND ----------

import pandas as pd

# COMMAND ----------

salarios={
    "Nombre":["Juan","Pedro","Maria","Pepe","Oli"],
    "Edad":[23,30,60,26,35],
    "Salario":[1000,12000,17000,1200,30000],
    "Genero":["M","M","F","M","F"]
}

# COMMAND ----------

data_salarios=pd.DataFrame(salarios)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Diferencia entre salario min y max 

# COMMAND ----------

salario_max = data_salarios.max()[2]
salario_min = data_salarios.min()[2]

print(f'El salario máximo es {salario_max} y le pertenece a {data_salarios.max()[0]}. El salario mínimo es {salario_min} y le pertenece a {data_salarios.min()[0]}. La diferencia es {salario_max - salario_min}')

# COMMAND ----------

# MAGIC %md
# MAGIC ##Estadísticos descriptivos

# COMMAND ----------

data_salarios.describe()
