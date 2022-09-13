# Databricks notebook source
# MAGIC %md
# MAGIC ##Ejercicio:Calculadora

# COMMAND ----------

import math
#Programar una calculadora con 4 operaciones básicas usando clases y objetos

#definir clase calculadora y sub-clases de operaciones

class calculadora (): 
    '''Clase que recibe dos números y calcula operaciones aritméticas simples'''
    
    def __init__(self,n1,n2): #Siempre que se espera que el usuario ingrese data, se requiere un __init__
        self.n1= n1#Deben ser double para poder hacer división con decimales
        self.n2= n2
    
    def suma(self):
        suma=self.n1+self.n2
        return suma

    def resta(self):
        resta=self.n1-self.n2
        return resta

    def multi(self):
        multi=self.n1*self.n2
        return multi
    
    def div(self):
        #self.n1= float(self.n1)#Deben ser double para poder hacer división con decimales
        #self.n2= float(self.n2)
        div=self.n1/self.n2
        return div

    def sqr(self):
        n1sqr = math.sqrt(self.n1)
        n2sqr = math.sqrt(self.n2)
        return n1sqr, n2sqr 
    
    def potencia(self):
        potencia = self.n1**self.n2
        return potencia
        
        
n_1 = 4
n_2 = 16
        
calculos = calculadora(n_1,n_2)
print(f'- Los numeros ingresados son: {n_1} y {n_2}. \n- La suma es {calculos.suma()}, la resta es {calculos.resta()}, la multiplicación es {calculos.multi()} y la división es {calculos.div()}. \n- Las raíces cuadradas son {calculos.sqr()[0]} y {calculos.sqr()[1]} respectivamente.\n- {n_1} elevado a la {n_2}° potencia es {calculos.potencia()}.')

