# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
		Módulo que contiene los métodos que permitirán insertar, modificar y
		eliminar actores.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar.
from model import db,func,Actores, ActoresHistorias

#.-----------------------------------------------------------------------------.


# Clase que tendra las diferentes funcionalidades de la tabla "Actores".
class clsActor():

	#.-------------------------------------------------------------------------.
	
	def insertar(self, idProducto, nombre, descripcion):
		"""
			@brief Funcion que permite insertar un nuevo actor en 
					la base de datos.

			@param idProducto: identificador del producto al que pertenecerá el 
							   actor.						
			@param nombre: nombre del actor a insertar.
			@param descripcion: especificacion del actor a insertar.

			@return True si se insertó correctamente el actor deseado. En caso 
					contrario, retorna False.
		"""

		# Booleanos que indican si los parametros son del tipo correspondiente.
		descripcionStr = type(descripcion) == str
		nombreStr = type(nombre) == str
		idProductoInt  = type(idProducto) == int

		if ( descripcionStr and nombreStr and idProductoInt ):
			# Booleanos que indican si los parametros tienen el tamaño valido.
			nombreLongitud = 1 <= len(nombre) <= 50
			descripcionLongitud = 1 <= len(descripcion) <= 500
			idProductoPositivo = idProducto > 0
		
			if (nombreLongitud and descripcionLongitud and idProductoPositivo):

				# Ultimo id en la base de datos correspondiente	
				ultimoId = db.session.query(func.max(Actores.identificador)).\
								first()
				identificador = ultimoId[0]

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				identificador = 1 if identificador == None else identificador + 1

				actorNuevo = Actores(idProducto, identificador,nombre, descripcion)
				db.session.add(actorNuevo)
				db.session.commit()
				return( True )

		return( False )
		
	#.-------------------------------------------------------------------------.
	
	def buscarId(self,identificador):
		"""
			@brief Funcion que realiza la busqueda del actor cuyo identificador
				   sea "identificador".
		
			@param identificador: id del actor a buscar.
			
			@return tupla que contiene la información del actor buscado. En caso
					contrario retorna None.
		"""
		
		# Booleano que indica si el parámetro es del tipo correspondiente.
		idInt = type(identificador) == int		

		if ( idInt ):
			idBuscado = db.session.query(Actores).\
							filter(Actores.identificador == identificador).\
							first()	
			return( idBuscado )
		return( None )
	
	#.-------------------------------------------------------------------------.

	def buscarNombre(self, nombre):
		"""
			@brief Funcion que realiza la busqueda de los actores cuyo nombre
				   sea "nombre".

			@param nombre: nombre del actor a buscar.
			
			@return tupla que contiene la información del actor buscado. En caso
					contrario retorna None. 

		"""

		# Booleano que indica si el parametro es del tipo correspondiente.
		nombreStr = type(nombre) == str
		
		if ( nombreStr ):
			nombreBuscado = db.session.query(Actores).\
					filter(Actores.nombre == nombre).\
					first()
			return (nombreBuscado)
		return( None )
		
	#.-------------------------------------------------------------------------.

	def modificar(self, identificador, nombre, descripcion):
		"""
			@brief Función que modifica los datos del actor cuyo id sea 
				   "identificador".
				
			@param identificador: id del actor a modificar.
			@param nombre: nuevo nombre para el actor dado.
			@param descripcion: nueva descripcion para el actor dado.
			
			@return True si se modifico correctamente el actor dado. En caso 
					contrario retorna False.
		"""
		
		# Booleanos que indican si los parámetros son del tipo correspondiente.
		nombreStr = type(nombre) == str
		descripcionStr = type(descripcion) == str
		idInt = type(identificador) == int
		
		if ( nombreStr and idInt and descripcionStr ):
			# Booleanos que indican si se cumplen los limites.
			nombreLongitud 	= 1 <= len(nombre) <= 50
			idPositivo 	= identificador > 0
			descripcionLongitud = 1 <= len(descripcion) <= 500
			
			if ( nombreLongitud and idPositivo and descripcionLongitud ):
				idBuscado = self.buscarId(identificador)
				nombreBuscado = self.buscarNombre(nombre)
				
				if ( idBuscado != None):

					if (nombreBuscado == None):
						db.session.query(Actores).\
							filter(Actores.identificador == identificador).\
							update({'nombre': nombre,'descripcion': descripcion})
						db.session.commit()
						return( True )

					elif (nombreBuscado != None and idBuscado.nombre == nombre):
						db.session.query(Actores).\
							filter(Actores.identificador == identificador).\
							update({'descripcion':(descripcion)})
						db.session.commit()
						return( True )
		return( False )
	

	#.-------------------------------------------------------------------------.

	def eliminar(self, identificador):
		"""
			@brief Función que permite eliminar una actor cuyo id
				   sea "identificador".
			
			@return True si se eliminó el actor dado. De lo contrario retorna
					False.
		"""

		idInt = type(identificador) == int
		
		if (idInt):
			idPositivo = identificador >0
			
			if ( idPositivo ):
				actorBuscado = db.session.query(Actores).\
						filter(Actores.identificador == identificador).\
						first()

				if ( actorBuscado != None):

						actorContenido = db.session.query(ActoresHistorias).\
									  filter(ActoresHistorias.idActores == identificador).\
									  first()


						if ( actorContenido == None):

							db.session.delete(actorBuscado)
							db.session.commit()
							return ( True )
			
		return ( False )
