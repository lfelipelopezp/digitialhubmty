# Databricks notebook source
# MAGIC %md
# MAGIC ##Definición de nodos y vecinos

# COMMAND ----------

# MAGIC %md
# MAGIC ####Librerías

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC ####Funciones

# COMMAND ----------

def CrearListaNodo(nodo):
    globals()['arr_' + nodo] = []
    
def AgregarVecino(nodo, nodo_vecino):
    globals()['arr_' + nodo].append(nodo_vecino)


# COMMAND ----------

# MAGIC %md
# MAGIC ####Usuario: Defina lista con nodos

# COMMAND ----------

lista_nodos = ['A', 'B','C', 'D', 'F', 'G']

# COMMAND ----------

# MAGIC %md
# MAGIC ####Poblar Nodos con vecinos

# COMMAND ----------

#Nodo A
CrearListaNodo('A')
AgregarVecino('A', 'B')
AgregarVecino('A', 'C')
AgregarVecino('A', 'G')

#Nodo B
CrearListaNodo('B')
AgregarVecino('B', 'F')
AgregarVecino('B', 'G')

#Nodo C
CrearListaNodo('C')
AgregarVecino('C', 'A')
AgregarVecino('C', 'D')
AgregarVecino('C', 'G')

#Nodo D
CrearListaNodo('D')
AgregarVecino('D', 'F')
AgregarVecino('D', 'G')

#Nodo F
CrearListaNodo('F')

#Nodo G
CrearListaNodo('G')
AgregarVecino('G', 'A')
AgregarVecino('G', 'D')
AgregarVecino('G', 'F')

# COMMAND ----------

# MAGIC %md
# MAGIC ###Listas de Nodos y respectivos vecinos

# COMMAND ----------

print("Nodos y vecinos creados:\n")
for nodo in lista_nodos:
    print(f'Nodo_{nodo}: ' + str(globals()['arr_' + nodo]))


# COMMAND ----------

# MAGIC %md
# MAGIC ###Crear dropdown widgets con Or y De

# COMMAND ----------

#Crear lista de nodos origen

#dbutils.widgets.remove("Nodo Origen")
#dbutils.widgets.remove("Nodo Destino")

lista_nodos_origen = []

for i in range(len(lista_nodos)):
    if len(globals()['arr_' + lista_nodos[i]]) > 0:
        lista_nodos_origen.append(lista_nodos[i])

dbutils.widgets.dropdown("Nodo Origen", lista_nodos_origen[0], lista_nodos_origen)
dbutils.widgets.dropdown("Nodo Destino", lista_nodos[1], lista_nodos)


# COMMAND ----------

# MAGIC %md
# MAGIC ##Algoritmo

# COMMAND ----------

# MAGIC %md
# MAGIC ####Calcular caminos posibles

# COMMAND ----------

origen = dbutils.widgets.get("Nodo Origen").upper()
destino = dbutils.widgets.get("Nodo Destino").upper()
nodos_pasados = [origen]
caminos = []

for i in  globals()['arr_' + origen]:
    print("1-",i)
    camino_lv1 = [origen]
    if i == destino:
        camino_lv1.append(i) 
        print(camino_lv1)
        caminos.append(camino_lv1)
    elif i in nodos_pasados:
        continue
    else:
        nodos_pasados.append(i)
        camino_lv1.append(i) 
#-------lv2---------------------------------------------------------------------------------------------------------------------------------------------------------
        for j in globals()['arr_' + i]:
            camino_lv2 = camino_lv1[:]
            #print(camino_lv1)
            print("2-",j)
            if j == destino:
                camino_lv2.append(j) 
                print(camino_lv2)
                caminos.append(camino_lv2)
            elif j in nodos_pasados:
                continue  
            elif len(globals()['arr_' + j]) < 1:
                nodos_pasados.append(j)
                print('Termina 2 - Nodo vacío')
                continue   
            else:
                nodos_pasados.append(j)
                camino_lv2.append(j)
#-------lv3---------------------------------------------------------------------------------------------------------------------------------------------------------
                for k in globals()['arr_' + j]:
                    camino_lv3 = camino_lv2[:]
                    #print(camino_lv2)
                    print("3-",k) 
                    if k == destino:
                        camino_lv3.append(k) 
                        print(camino_lv3)
                        caminos.append(camino_lv3) 
                    elif k in nodos_pasados:
                        continue   
                    elif len(globals()['arr_' + k]) < 1 :
                        nodos_pasados.append(k)
                        print('Termina 3 - Nodo vacío')
                        continue  
                    else:
                        nodos_pasados.append(k)
                        camino_lv3.append(k)
#-------lv4---------------------------------------------------------------------------------------------------------------------------------------------------------
                        for l in globals()['arr_' + k]:
                            camino_lv4 = camino_lv3[:]
                            #print(camino_lv3)
                            print("4-",l)
                            #print(nodos_pasados)                            
                            if l == destino:
                                camino_lv4.append(l) 
                                print(camino_lv4)
                                caminos.append(camino_lv4)
                            elif l in nodos_pasados:
                                continue 
                            elif len(globals()['arr_' + l]) < 1:
                                nodos_pasados.append(l)
                                print('Termina 4 - Nodo vacío')
                                continue    
                            else:
                                nodos_pasados.append(l)
                                camino_lv4.append(l)
#-------lv5---------------------------------------------------------------------------------------------------------------------------------------------------------                        
                                for m in globals()['arr_' + l]:
                                    camino_lv5 = camino_lv4[:]
                                    #print(camino_lv4)
                                    print("5-",m)
                                    #print(nodos_pasados)                            
                                    if m == destino:
                                        camino_lv5.append(m) 
                                        print(camino_lv5)
                                        caminos.append(camino_lv5)
                                    elif m in nodos_pasados:
                                        continue 
                                    elif len(globals()['arr_' + m]) < 1:
                                        nodos_pasados.append(m)
                                        print('Termina 5 - Nodo vacío')
                                        continue    
                                    else:
                                        nodos_pasados.append(m)
                                        camino_lv5.append(m)
#-------lv6---------------------------------------------------------------------------------------------------------------------------------------------------------                       
                                        for n in globals()['arr_' + m]:
                                            camino_lv6 = camino_lv5[:]
                                            #print(camino_lv5)
                                            print("6-",n)
                                            #print(nodos_pasados)                            
                                            if n == destino:
                                                camino_lv6.append(n) 
                                                print(camino_lv6)
                                                caminos.append(camino_lv6)
                                            elif n in nodos_pasados:
                                                continue 
                                            elif len(globals()['arr_' + n]) < 1:
                                                nodos_pasados.append(n)
                                                print('Termina 6 - Nodo vacío')
                                                continue    
                                            else:
                                                nodos_pasados.append(n)
                                                camino_lv6.append(n) 
#-------lv7---------------------------------------------------------------------------------------------------------------------------------------------------------

                                                for o in globals()['arr_' + n]:
                                                    camino_lv7 = camino_lv6[:]
                                                    #print(camino_lv6)
                                                    print("7-",o)
                                                    #print(nodos_pasados)                            
                                                    if o == destino:
                                                        camino_lv7.append(o) 
                                                        print(camino_lv7)
                                                        caminos.append(camino_lv7)
                                                    elif o in nodos_pasados:
                                                        continue 
                                                    elif len(globals()['arr_' + o]) < 1:
                                                        nodos_pasados.append(o)
                                                        print('Termina 7 - Nodo vacío')
                                                        continue    
                                                    else:
                                                        nodos_pasados.append(o)
                                                        camino_lv6.append(o) 
#-------lv8---------------------------------------------------------------------------------------------------------------------------------------------------------                        
                                                        for p in globals()['arr_' + o]:
                                                            camino_lv8 = camino_lv7[:]
                                                            #print(camino_lv7)
                                                            print("8-",p)
                                                            #print(nodos_pasados)                            
                                                            if p == destino:
                                                                camino_lv8.append(p) 
                                                                print(camino_lv8)
                                                                caminos.append(camino_lv8)
                                                            elif p in nodos_pasados:
                                                                continue 
                                                            elif len(globals()['arr_' + p]) < 1:
                                                                nodos_pasados.append(p)
                                                                print('Termina 8 - Nodo vacío')
                                                                continue    
                                                            else:
                                                                nodos_pasados.append(p)
                                                                camino_lv6.append(p)                                                         
#-------lv9---------------------------------------------------------------------------------------------------------------------------------------------------------                        
                                                                for q in globals()['arr_' + p]:
                                                                    camino_lv9 = camino_lv8[:]
                                                                    #print(camino_lv8)
                                                                    print("9-",q)
                                                                    #print(nodos_pasados)                            
                                                                    if q == destino:
                                                                        camino_lv9.append(q) 
                                                                        print(camino_lv9)
                                                                        caminos.append(camino_lv9)
                                                                    elif q in nodos_pasados:
                                                                        continue 
                                                                    elif len(globals()['arr_' + q]) < 1:
                                                                        nodos_pasados.append(q)
                                                                        print('Termina 9 - Nodo vacío')
                                                                        continue    
                                                                    else:
                                                                        nodos_pasados.append(q)
                                                                        camino_lv6.append(q)    
#-------lv10--------------------------------------------------------------------------------------------------------------------------------------------------------                    
                                                                        for r in globals()['arr_' + q]:
                                                                            camino_lv10 = camino_lv9[:]
                                                                            #print(camino_lv9)
                                                                            print("10-",r)
                                                                            #print(nodos_pasados)                            
                                                                            if r == destino:
                                                                                camino_lv10.append(r) 
                                                                                print(camino_lv10)
                                                                                caminos.append(camino_lv10)
                                                                            elif r in nodos_pasados:
                                                                                continue 
                                                                            elif len(globals()['arr_' + r]) < 1:
                                                                                nodos_pasados.append(r)
                                                                                print('Termina 10 - Nodo vacío')
                                                                                continue    
                                                                            else:
                                                                                nodos_pasados.append(r)
                                                                                camino_lv6.append(r)  
                                                        
                                                        

# COMMAND ----------

# MAGIC %md
# MAGIC ####Asignación de costos y pesos

# COMMAND ----------

#Leer CSV con costos entre nodos
path = '/dbfs/mnt/dpo/AI_Factory/MonterreyDigitalHub/Proyecto Final/Gaby y Felipe/PesosNodos_ProyectoFinalMontereyDigHub_Gaby_LF.csv'
df_pesos = pd.read_csv(path)
display(df_pesos)

# COMMAND ----------

#Asignar costo total a cada camino posible
print(caminos)
costos_totales = []

for i in range(len(caminos)):
    acumulador_costo = 0
    for j in range(1,len(caminos[i])):
        origen = caminos[i][j - 1]
        destino = caminos[i][j]
        #print(f'El origen es {origen} y el destino es {destino}')
        costo = df_pesos['costo'][(df_pesos['nodo_origen'] == origen) & (df_pesos['nodo_destino'] == destino)].iloc[0]
        #print(costo)
        acumulador_costo = acumulador_costo + costo
    
    #print(acumulador_costo)
    costos_totales.append(acumulador_costo)      

print(costos_totales)



# COMMAND ----------

# MAGIC %md
# MAGIC ##Respuestas

# COMMAND ----------

#Imprime las respuestas, revisando si existe un sólo camino o más para el OR-DE.
if len(caminos) > 1:
    longitudes = []                                
    for list in caminos:
        longitudes.append(len(list))

    print("\nCaminos posibles:",caminos)
    print("Costos de los caminos:",costos_totales)
    
    #Mostrar costos min y max    
    min_cost =  min(costos_totales)
    max_cost = max(costos_totales)

    index_min = min(range(len(costos_totales)), key=costos_totales.__getitem__)
    index_max = max(range(len(costos_totales)), key=costos_totales.__getitem__)

    #Responder preguntas
    print(f'\nExisten {len(caminos)} forma(s) de llegar desde el nodo {origen} al nodo {destino}.') 
    print(f'\nEl camino más corto es {caminos[longitudes.index(min(longitudes))]} y pasas por {longitudes[longitudes.index(min(longitudes))]-2} nodo(s) intermedios.')  
    print(f'El camino más largo es {caminos[longitudes.index(max(longitudes))]} y pasas por {longitudes[longitudes.index(max(longitudes))]-2} nodo(s) intermedios.')  
    print(f'\nEl camino con menor costo es {caminos[index_min]} y cuesta {min_cost}. El camino con el mayor costo es {caminos[index_max]} y cuesta {max_cost}.')

else:
    print(f'\nSolo existe una forma de llegar desde el nodo {origen} al nodo {destino}.')
    print(f'\nEl camino es {caminos[longitudes.index(min(longitudes))]} y pasas por {longitudes[longitudes.index(min(longitudes))]-2} nodo(s) intermedios. El costo del camino es {costos_totales[0]}.')

