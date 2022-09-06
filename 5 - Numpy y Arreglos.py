# Databricks notebook source
# MAGIC %md
# MAGIC ##Numpy

# COMMAND ----------

n = [1,2,3]
type(n)

# COMMAND ----------

#importat numpy
import numpy as np

# COMMAND ----------

m = np.array(n)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Actividad: Arrays Unidimensionales

# COMMAND ----------

#Crear vector con valores 3 a mi edad
edad = 26
array = []
for i in range(3, edad +1):
    array = np.append (array, i)

#Alternativo
array= np.arange(3, edad)
    
    
#Crear arreglo con valores [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    
arr_1 = [0, 1, 2, 3, 4]
arr_2 = ar_1

arr = np.append(arr_1, arr_2)

#Ordenar ese arreglo final
arr.sort()
arr


# COMMAND ----------

# MAGIC %md
# MAGIC ##Arreglos de dos dimensiones

# COMMAND ----------

#Definir arreglo 2D
bidim = np.array([[1,2,3],[4,5,6]])

# COMMAND ----------

#tamaño del arreglo
bidim.shape

# COMMAND ----------

#Obtener elemento del arreglo
bidim[1,1]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicios con arreglos 2D

# COMMAND ----------

#Crear arreglo con numeros consecutivos
f = np.arange(3,31)
f

# COMMAND ----------

#Crear arreglo con numeros consecutivos con salto
f = np.arange(3,31, 2)
f

# COMMAND ----------

#crear un arreglo 5x5 con numeros cosecutivos
h = np.reshape(np.array(range(1,26)),(5,5))
h

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 2 - Matriz identidad y 2D

# COMMAND ----------

#Crear matriz 2D 3X3 con valores de 0 a 8
m = np.reshape(np.array(range(0,9)),(3,3))
m = np.array(range(0,9)).reshape((3,3))
m

# COMMAND ----------

#matriz identidad 6x6

m = np.identity(6)
m
