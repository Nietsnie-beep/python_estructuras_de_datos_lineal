class Millas:
	def __init__(self):
		self._distancia = 0

	# Función get para obtener el valor de _distancia
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función set para definir el valor de _distancia
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# Función para eliminar el atributo _distancia
	def eliminar_distancia(self):
		del self._distancia
		print('eliminando propiedades')
	#distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.definir_distancia(100)

# Obtenemos su atributo distancia
"""avion.eliminar_distancia()"""
print(avion.obtener_distancia())
