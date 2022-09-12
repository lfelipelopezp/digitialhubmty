# Databricks notebook source
# MAGIC %md
# MAGIC ##Ejercicio:Calculadora

# COMMAND ----------

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
        self.n1= float(self.n1)#Deben ser double para poder hacer división con decimales
        self.n2= float(self.n2)
        div=self.n1/self.n2
        return div
        
n_1 = 10
n_2 = 3
        
calculos = calculadora(n_1,n_2)
print(f'Los numeros ingresados son: {n_1} y {n_2}. \nLa suma es {calculos.suma()}, la resta es {calculos.resta()}, la multiplicación es {calculos.multi()} y la división es {calculos.div()} ')

