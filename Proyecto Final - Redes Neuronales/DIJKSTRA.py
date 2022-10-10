# Databricks notebook source
# MAGIC %md
# MAGIC ## Librerías

# COMMAND ----------

import math

# COMMAND ----------

# MAGIC %md
# MAGIC ## Código

# COMMAND ----------

class Vertice:
	#Clase que define los vértices de los gráficas
	def __init__(self, i):
		self.id = i #identificador
		self.vecinos = [] # Los vecinos
		self.visitado = False #visitado = flag para saber si fue visitado o no
		self.padre = None #Cual es el padre de ese vertice
		self.costo = float('inf') #atributo distancia

	def agregarVecino(self, v, p): #Vecino, vértice y arista
		#Método que agrega los vertices que se encuentre conectados por una arista a la lista de vecinos 
		#de un vertice, revisando si éste aún no se encuentra en la lista de vecinos
		if v not in self.vecinos:
			self.vecinos.append([v, p]) #Se almacena en la lista de vecinos (índice, peso de arista)

# COMMAND ----------

#Clase que define los vértices de las gráficas
class Grafica:
	def __init__(self):
		#vertices = diccionario con los vertices de la grafica
		self.vertices = {}

	def agregarVertice(self, id):
		#Método que agrega vértices, recibiendo el índice y la heuristica (para A* puede que no se reciba) 
		#revisando si éste no existe en el diccionario de vértices
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):  #(self, puntos de, vertices, peso de arista)
		#Método que agrega aristas, recibiendo el índice de dos vertices y revisando si existen estos en la lista
		#de vertices, además de recibir el peso de la arista , el cual se asigna a ambos vértices por medio del método
		#agregar vecino
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)
	
	# Recibe punto inicial y final, indica por cuales nodos debemos de visitar
	def camino(self, a, b):
		#Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
		#lista con los vértices con el menor costo
		camino = []
		actual = b
		while actual != None: #mientras que sea diferente
			camino.insert(0, actual) #inserta en camino nodo actual al principio de la lista
			print("Del vertice "+ str(self.vertices[actual].padre) + " al vertice " + str(actual) + " tiene un costo acumulado de:  "+ str(self.vertices[actual].costo))
			actual = self.vertices[actual].padre
		return [camino, self.vertices[b].costo] #regresa el camino que se debe de seguir

	#Creación de función minimo
	def minimo(self, l):
		#Método que recibe la lista de los vertices no visitados, revisa si su longitud es mayor a cero(indica que 
		#aún hay vértices sin visitar), y realiza comparaciones de los costos de cada vértice en ésta lista para encontrar
		#el de menor costo
		if len(l) > 0:  #checa si tiene elementos la lista
			m = self.vertices[l[0]].costo  #distancia que esta en la posición cero de nuestra arista (último costo)
			v = l[0]  #nodo que esta en posición cero de la arista(último)
			for e in l: #búsqueda lineal para encontrar el mínimo
				if m > self.vertices[e].costo:
					m = self.vertices[e].costo #si es menor de actualiza m con el nuevo variable
					v = e #se actualiza
			return v #se regresa nodo con menor distancia
		return None

	def dijkstra(self, a): #vertice
		if a in self.vertices: # Verificar que el vertice este dentro del recorrido
			# 1 y 2
			self.vertices[a].costo = 0 #costo inicial del vertice 1 = 0
			actual = a #nodo actual
			noVisitados = [] #lista vacia
			
			for v in self.vertices: #recorrer el resto de los nodos
				if v != a: #primero se checa que "v" no sea "a"
					self.vertices[v].costo = float('inf') #se le pone el costo de infinito para todos los nodos de infinito
				self.vertices[v].padre = None 
				noVisitados.append(v) #agregar conjunto de no visitados a todos los vertices 
				# ya se cumplieron los pasos 1 y 2

			#Paso 3
			while len(noVisitados) > 0: #mientras que "no visitados" tenga elementos 
				#Paso4
				for vec in self.vertices[actual].vecinos:  #recorrer cada vecino de actual
					if self.vertices[vec[0]].visitado == False:  #considerar vecinos no visitados
						# 4.a
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo: #se actualiza valor y se suma el peso del arista y esta es menor entonces se guarda
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]  # se hace el cambio si se cumple
							self.vertices[vec[0]].padre = actual #padre actual del siguiente vecino(cambia el padre)

				# Paso 5
				self.vertices[actual].visitado = True #se marca el nodo actual a visitado
				noVisitados.remove(actual) #se quita del no vistado

				# Paso 6
				actual = self.minimo(noVisitados) #se actualiza variable actual, 
				#donde con el mínimo se le envía el conjunto de no visitados
		else:
			return False

# COMMAND ----------

# MAGIC %md
# MAGIC ## Main

# COMMAND ----------

#Clase princial
class main:
	g = Grafica()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarArista(1, 2, 5) #vertices de arista y sus pesos
	g.agregarArista(1, 3, 3)
	g.agregarArista(1, 6, 11)
	g.agregarArista(3, 1, 3)#
	g.agregarArista(6, 1, 11)#
	g.agregarArista(2, 6, 15)
	g.agregarArista(2, 5, 12)
	g.agregarArista(3, 4, 4)
	g.agregarArista(3, 6, 9)
	g.agregarArista(2, 5, 12)
	g.agregarArista(6, 5, 10)

	print("\n\nLa mejor ruta con cada uno de los pasos de nodo a nodo es: ")
	g.dijkstra(1) #indice del vertice punto inciial
	print(g.camino(1, 5)) #nodo de donde a donde
