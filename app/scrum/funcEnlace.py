# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
		Módulo que contiene los métodos que permitirán insertar y modificar
		enlaces.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func, Enlaces, Productos,Historias

#.-----------------------------------------------------------------------------.

# Clase que tendrá las diferentes funcionalidades de la tabla "Enlaces"
class clsEnlace():

	#.-------------------------------------------------------------------------.
	
	def insertar(self, idProducto, idEpica):
		"""
			@brief Función que permite crear un nuevo enlace entre dos historias
				   en la base de datos.

			@param idProducto: identificador del producto en donde se creará el 
							   enlace.
			@param idEpica: identificador de la historia que será épica de la 
							actual.

			@return True si se creó correctamente el enlace deseado. En caso 
					contrario retorna False.
		"""

		# Booleanos que indican si los parámetros son del tipo correspondiente.
		idProductoInt = type(idProducto) == int
		idEpicaInt = type(idEpica) == int  
		
		if ( idProductoInt and idEpicaInt ):
			
			idBuscado = db.session.query(Productos.identificador).\
							filter(Productos.identificador == idProducto).first()
			# Como idBuscado es una tupla entonces se accede al idValor deseado.
			idProductoBuscado = idBuscado[0]
			
			if (idProductoBuscado != None):		

				# Se busca el id de la última historia creada.
				idHistoriaUltima = db.session.query(func.max(Historias.identificador))
				idHistoria = idHistoriaUltima[0]
				idHistoria = idHistoria[0]
		
				idHistoria = 1 if idHistoria == None else idHistoria + 1
		
				# Se busca el id del último enlace creado.
				idEnlaceUltimo = db.session.query(func.max(Enlaces.identificador))
				identificador = idEnlaceUltimo[0]
				identificador = identificador[0]
		
				identificador = 1 if identificador == None else identificador + 1
		
				# Se procede a generar la lista de enlaces.
				enlacesActuales = db.session.query(Enlaces).all()
				listaEnlace = {}

				for enlace in enlacesActuales:
					if (enlace.idClave in listaEnlace):
						listaEnlace[enlace.idClave] += [enlace.idValor]		
					else:
						listaEnlace[enlace.idClave] = [enlace.idValor]
			
					if not(enlace.idValor in listaEnlace):
						listaEnlace[enlace.idValor] =[]
					
					if (enlace.idClave == idEpica):
						if not(idHistoria in listaEnlace[enlace.idClave]):
							listaEnlace[enlace.idClave] += [idHistoria]

						if not( idHistoria in listaEnlace):
							listaEnlace[idHistoria] = []
			
				existeCiclo = self.existenciaCiclo(listaEnlace)
		
				if not(existeCiclo):
					enlaceNuevo = Enlaces(identificador, idProducto, idEpica, 
											idHistoria)
					db.session.add(enlaceNuevo)
					db.session.commit()
					return( True )
		return( False )

   #.--------------------------------------------------------------------------.

	def modificar(self, idViejaEpica, idNuevaEpica, idHistoria):
		"""
			@brief Función que permite modificar un enlace dado.

			@param idViejaEpica: identificador de la épica actual.
			@param idNuevaEpica: identificador de la nueva épica.
			@param idHistoria: identificador de la historia a modificar. 

			@return True si se modificó correctamente el enlace deseado. En caso 
					contrario retorna False.
		"""

 		# Booleanos que indican si los parámetros son del tipo correspondiente.
		idViejaEpicaInt = type(idViejaEpica) == int
		idNuevaEpicaInt = type(idNuevaEpica) == int
		idHistoriaInt   = type(idHistoria)   == int

		if ( idViejaEpicaInt and idNuevaEpicaInt and idHistoriaInt ):

			# Se procede a generar la lista de enlaces.
 			enlacesActuales = db.session.query(Enlaces).all()
 			listaEnlace = {}

 			for enlace in enlacesActuales:

 				if (( enlace.idClave != idViejaEpica ) or 
					( enlace.idClave == idViejaEpica and enlace.idValor != idHistoria)):

 					if (enlace.idClave in listaEnlace):
 						listaEnlace[enlace.idClave] += [enlace.idValor]
 					else:
 						listaEnlace[enlace.idClave] = [enlace.idValor]

 					if not(enlace.idValor in listaEnlace):
 						listaEnlace[enlace.idValor] =[]

 					if (enlace.idClave == idNuevaEpica):
 						if not(idHistoria in listaEnlace[enlace.idClave]):
 							listaEnlace[enlace.idClave] += [idHistoria]

 						if not( idHistoria in listaEnlace):
 							listaEnlace[idHistoria] = []


 				elif (enlace.idClave == idViejaEpica and enlace.idValor == idHistoria):
 					listaEnlace[idHistoria] = []
		
		

		 	existeCiclo = self.existenciaCiclo(listaEnlace)
		 		
	 		if not(existeCiclo):
	 			db.session.query(Enlaces).\
	 				filter(Enlaces.idClave == idViejaEpica, Enlaces.idValor == idHistoria).\
	 				update({'idClave':(idNuevaEpica)})
	 			db.session.commit()
	 			return( True )

		return( False )  	

   #.--------------------------------------------------------------------------.

	def existenciaCiclo(self, grafo):
		"""
			@brief Función que permite verificar si existe un ciclo en un grafo
				   dado.

			@param grafo: estructura en donde se verificará la existencia del 
						  ciclo.

			@return True si existe un ciclo en el grafo. En caso contrario 
					retorna False.
		"""
		
		# Se inician todos los "vertices" con el color blanco.
		color = { u : "blanco" for u in grafo  } 
		encontrarCiclo = [False]

		for vertice in grafo:
			if color[vertice] == "blanco":
				self.dfs_visit(grafo, vertice, color, encontrarCiclo)
			if encontrarCiclo[0]:
				break
		return encontrarCiclo[0]
     
    #-------

	def dfs_visit(self, grafo, vertice, color, encontrarCiclo):
		"""
			@brief Función que realiza la busqueda en profundidad en un grafo 
					dado.

			@param grafo: estructura a la que se le aplicará DFS.
			@param vertice: vertice en donde se iniciará el DFS.
			@param color: diccionario que tiene almacenado los colores actuales 
						  de los vertices.
			@param encontrarCiclo: resultado actual de la busqueda del ciclo. 

			@return True si existe un ciclo en el grafo. En caso contrario 
					retorna False.
		"""

		if encontrarCiclo[0]:                         
			return
		color[vertice] = "gris"
		for adyacente in grafo[vertice]:
			if color[adyacente] == "gris":                 
				encontrarCiclo[0] = True       
				return
			if color[adyacente] == "blanco":                 
				self.dfs_visit(grafo, adyacente, color, encontrarCiclo)
		color[vertice] = "negro"                         

    #.-------------------------------------------------------------------------.