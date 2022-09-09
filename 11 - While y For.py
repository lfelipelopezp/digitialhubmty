# Databricks notebook source
# MAGIC %md
# MAGIC ##Ejercicio estacionamiento ciclo While

# COMMAND ----------

# MAGIC %md
# MAGIC ##Ejercicio funciones

# COMMAND ----------

import math

# COMMAND ----------

# ax^2 + bx + c = 0
# x^2 +2x + 15 = 0

a = 1
b = 2
c = 15

def chicharronera(a,b,c):
    x1 = (-b + math.sqrt(b*b + 4*a*c))/2*a
    x2 = (-b - math.sqrt(b*b + 4*a*c))/2*a
    return x1, x2

print(chicharronera(a,b,c))
print(f'X1 = {chicharronera(a,b,c)[0]} y X2 = {chicharronera(a,b,c)[1]}')

