# Databricks notebook source
# MAGIC %md
# MAGIC ##Actividad 8: Operaciones de Edad

# COMMAND ----------

#1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo?
#24 = 2*edad
mi_edad = 24/2

#2.- A un tercio de la edad de mi hermana la disminuyo en 15 años. Tengo 6 años. ¿Qué edad tiene?
#6 = edad_hermana/3-15
edad_hermana = (6+15)*3

#3.-Determina quién es más grande
if mi_edad > edad_hermana:
    print("Yo soy mayor")
else:
    print("Mi hermana es mayor")


