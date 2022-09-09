# Databricks notebook source
# MAGIC %md
# MAGIC ##Ejercicio - Edad y genero

# COMMAND ----------

nombres_genero = {'Juan':'es M', 'María':'es F', 'Pedro':'es M', 'Olivia':'es F'}

# COMMAND ----------

edad = 29
nombre = 'Adolf'
gen_usuario = 'es M'

if edad > 18:
    r = 'mayor de edad'
else:
    r = 'menor de edad'


if nombre in nombres_genero.keys():
    genero = nombres_genero[nombre]
else:
    genero = 'no se puede saber, dado que no está en nuestro registro.'
    nombres_genero[nombre] = gen_usuario
      


print(f'Hola {nombre}, eres {r} y tu genero {genero}')

print("\n")
print("Diccionario actualizado:")
print(nombres_genero)



