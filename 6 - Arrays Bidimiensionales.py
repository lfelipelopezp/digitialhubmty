# Databricks notebook source
# MAGIC %md
# MAGIC ##Actividad: Arrays Bidimensionales

# COMMAND ----------

import numpy as np

# COMMAND ----------

#Crear matriz 2D 3X3 con valores de 0 a 8
m = np.reshape(np.array(range(0,9)),(3,3))
m = np.array(range(0,9)).reshape((3,3))
print("Matriz 3x3 0 a 8:")
print(m)

# COMMAND ----------

#matriz identidad 6x6

m = np.identity(6)

print("Matriz Identidad 6x6")
print(m)
