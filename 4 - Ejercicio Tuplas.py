# Databricks notebook source
# MAGIC %md
# MAGIC ##Ejercicio Tuplas

# COMMAND ----------

#Crear Tupla
tuple_ej = ('hola', 1, False, 1000, ['a', 'b'])

#Cambiar tupla a lista

#for i in range(len(tuple_ej)):
#    lista.append(tuple_ej[i])

lista = list(tuple_ej)

#Convertir lista a diccionario
diccionario = {}

for i in range(5):
    diccionario[i+1] = lista[i]
    #diccionario.update({"ID": i+1, "Elemento": lista[i]})

diccionario
