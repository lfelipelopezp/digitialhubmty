# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

dict_1={
    "Nombre":["Ringo","John","Paul","George","Yoko"],
    "Edad":[45,34,42,38,47],
    "Salario":[12000,14000,13000,11000,10000],
    "Genero":["M","M","M","M","F"]
}

# COMMAND ----------

data=pd.DataFrame(dict_1)

# COMMAND ----------

data.head()

# COMMAND ----------

datos_categoricos=data.select_dtypes(exclude=[np.number]) #Excluir info numerica y seleccionar el resto
print("La base contiene {0} datos categóricos".format(datos_categoricos.shape[1]))

# COMMAND ----------

data.dtypes #Tipo de datos de cada columna

# COMMAND ----------

data.describe()

# COMMAND ----------

data.median(numeric_only=True)

# COMMAND ----------

data.count()

# COMMAND ----------

data.mean(numeric_only=True)

# COMMAND ----------

data.mode(numeric_only=True)

# COMMAND ----------

data.std(numeric_only=True)

# COMMAND ----------

data.sum()

# COMMAND ----------

data.max()

# COMMAND ----------

data.min()

# COMMAND ----------

data[data["Edad"]==data["Edad"].min()]

# COMMAND ----------

data["Edad"].abs

# COMMAND ----------

data.prod(numeric_only=True)

# COMMAND ----------

data.cumsum()

# COMMAND ----------

data["Edad"].cumprod()

# COMMAND ----------

data

# COMMAND ----------

data2=pd.get_dummies(data[["Genero"]])

# COMMAND ----------

data2

# COMMAND ----------

data2.value_counts()

# COMMAND ----------


