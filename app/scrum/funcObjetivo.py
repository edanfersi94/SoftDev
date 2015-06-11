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
		eliminar objetivos.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func, Objetivos, ObjHistorias

#.-----------------------------------------------------------------------------.

# Clase que tendra las diferentes funcionalidades de la tabla "Objetivo".
class clsObjetivo():

	#.-------------------------------------------------------------------------.
	
	def insertar(self, idProducto, descripcion,transversalidad):
		"""
			@brief Funcion que permite insertar un nuevo objetivo en la base de
				   datos.
			
			@param idProducto : Producto al que pertenecerá el objetivo.			
			@param descripcion: Descripcion del objetivo a insertar.
			@param transversalidad: entero entre 0 y 1 que indica si el objetivo
									es transversal.
			
			@return True si se insertó el objetivo dado. De lo contrario False.
		"""


		# Booleanos que indican si los parámetros son del tipo correspondiente.
		transversalidadInt = type(transversalidad) == int 
		descripcionStr = type(descripcion) == str
		idProductoInt  = type(idProducto) == int
	
		if ( transversalidadInt and idProductoInt and descripcionStr):
			# Booleanos que indican si se cumplen los limites.
			descripcionLongitud = 1 <= len(descripcion) <= 500
			idProductoPositivo  = idProducto > 0
			transversalidadLongitud = -1 < transversalidad < 2 
		
			if ( descripcionLongitud and idProductoPositivo and transversalidadLongitud ):
				
				# Búsqueda del último id en la base de datos correspondiente.	
				ultimoId = db.session.query(func.max(Objetivos.identificador)).\
							first()
				identificador  = ultimoId[0]

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				identificador = 1 if identificador == None else identificador + 1

				objetivoNuevo = Objetivos(idProducto, identificador ,descripcion,
										 transversalidad)
				db.session.add(objetivoNuevo)
				db.session.commit()
				return( True )
		
		return( False )
	
	#.-------------------------------------------------------------------------.
	
	def buscarId(self,identificador):
		"""
			@brief Funcion que realiza la busqueda del objetivo cuyo identificador
				   sea "identificador".
			
			@param identificador: id del objetivo a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. En caso
					cotrario retorna None.
		"""
		
		idInt = type(identificador) == int
		
		if ( idInt):
			idBuscado = db.session.query(Objetivos).\
					filter(Objetivos.identificador == identificador).\
					first()
			return( idBuscado )
		return( None )
	
	#.-------------------------------------------------------------------------.

	def modificar(self,identificador, descripcion,transversalidad):
		"""
			@brief Función que modifica los datos del objetivo cuyo id sea 
			       "identificador".
				
			@param identificador: id del objetivo a modificar.
			@param descripcion: nueva descripcion para el objetivo dada.
			@param transversalidad: entero entre 0 y 1 que indica si el objetivo
									es transversal.

			@return True si se modifico correctamente el objetivo dado. En caso
					con
		"""
		
		# Booleanos que indican si los parámetros son del tipo correspondiente.
		transversalidadInt = type(transversalidad) == int 
		descripcionStr = type(descripcion) == str
		idInt  = type(identificador) == int
		
		if ( idInt and descripcionStr and  transversalidadInt):
			# Booleanos que indican si se cumplen los limites.
			idPositivo 	= identificador > 0
			descripcionLongitud = 1 <= len(descripcion) <= 500
			transversalidadLongitud = -1 < transversalidad < 2 
			
			if ( idPositivo and descripcionLongitud and  transversalidadLongitud ):
				idBuscado = self.buscarId(identificador)
				
				if ( idBuscado != None ):
					db.session.query(Objetivos).\
						filter(Objetivos.identificador == identificador).\
						update({'descripcion': descripcion,
								'transversalidad':transversalidad})
					db.session.commit()	
					return( True )		
		return( False )	

#.-------------------------------------------------------------------------.	

	def eliminar(self, identificador):
		"""
			@brief Función que permite eliminar un objetivo cuyo id
				   sea "identificador".
			
			@return True si se eliminó el objetivo dado. De lo contrario retorna
					False.
		"""

		idInt = type(identificador) == int
		
		if (idInt):
			idPositivo = identificador >0
			
			if ( idPositivo ):
				objetivoBuscado = db.session.query(Objetivos).\
						filter(Objetivos.identificador == identificador).\
						first()

				if ( objetivoBuscado != []):

					objetivoContenido = db.session.query(ObjHistorias).\
									  	filter(ObjHistorias.idObjetivo == identificador).\
									  	first()
					
					if ( objetivoContenido == None):
					
						db.session.delete(objetivoBuscado)
						db.session.commit()
						return ( True )
			
		return ( False )
