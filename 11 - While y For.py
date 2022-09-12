# Databricks notebook source
# MAGIC %md
# MAGIC ##Ejercicio compras por cliente + Estacionamiento

# COMMAND ----------

#Crear un programa que permita al usuario ingresar el tiempo dentro en un estacionamiento , cortando el ingreso de datos cuando el usuario ingresa 0 minutos.

#NOTA: DADO QUE NO EXISTEN POPUPS EN DB, SE OMITIRÁ EL WHILE TIEMPO>0:

#Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad.
tiempo_min = 130

if tiempo_min < 0:
    print('Cantidad no válida. Ingrese nuevamente.')
else:
    #Ingresar una tarifa fija durante la primera hora (60 minutos) de $25 y $15 por cada hora adicional. 
    horas = tiempo_min//60
    minutos = tiempo_min - horas*60

    if minutos > 0:
        horas = horas + 1

    tarifa_primera_hora = 25
    tarifa_horas_extra = 15

    total_pago = tarifa_primera_hora + (horas -1) * tarifa_horas_extra

    #Al finalizar, informar el total a pagar teniendo en cuenta que, si el monto supera las 8 horas se aplica una tarifa fija de $200 extra. 

    if horas > 8:
        total_pago = total_pago + 200

    print(f'El total a pagar es de ${total_pago} con un total de {horas}h:{minutos}min.')


# COMMAND ----------

# MAGIC %md
# MAGIC ##Ejercicio funcion cuadrática

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

