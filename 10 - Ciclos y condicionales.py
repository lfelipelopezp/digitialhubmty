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




# COMMAND ----------

# MAGIC %md
# MAGIC ##Actividad: Bucle for en grupo

# COMMAND ----------

import random

dic_nom_par = {}
#print(dic_nom_par)

nombres = ['Juan', 'Pedro', 'Maria', 'Sofia']
parejas = ['Olivia', 'Gabriela', 'Cesar', 'David']

#Asigna un número aleatorio a tu compañero. Los guardarás en un diccionario, junto con el nombre de tu pareja.

for i in range(len(nombres)):
    dic_nom_par[nombres[i]] = {'Pareja': parejas[i], 'NoRandom': random.randint(0,10)}
#print(dic_nom_par)

#Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
numeros = []
keys = list(dic_nom_par.keys())

for i in range(len(keys)):
    norandom = dic_nom_par[keys[i]]['NoRandom']
    numeros.append(norandom)
    print(f'El nombre es {keys[i]} y su número aleatorio es {norandom}')
    

#Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.
print('\n')
print(f'El número más alto fue {max(numeros)} y el más pequeño {min(numeros)}')


# COMMAND ----------

dic_nom_par['Juan']['NoRandom']

