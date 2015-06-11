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
		eliminar acciones.
"""


#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func, Acciones, ActoresHistorias, Historias

#.-----------------------------------------------------------------------------.


# Clase que tendrá las diferentes funcionalidades de la tabla "Acciones".
class clsAccion():

	#.-------------------------------------------------------------------------.
	
	def insertar(self, idProducto, descripcion):
		"""
			@brief Función que permite insertar una nueva acción en la base de 
				   datos.
			
			@param idProducto : identificador del producto al que pertenecerá la 
								acción.
			@param descripcion: especificación de la acción a insertar.

			@return True si se insertó correctamente la acción deseada. En caso
					contrario retorna False.
		"""

		# Booleanos que indican si los parámetros son del tipo correspondiente.
		descripcionStr = type(descripcion) == str
		idProductoInt  = type(idProducto)  == int

		if ( descripcionStr and idProductoInt ):
			# Booleanos que indican si los parámetros tienen el tamaño válido.
			descripcionLongitud = 1 <= len(descripcion) <= 500
			idProductoPositivo  = idProducto > 0

			if ( descripcionLongitud and idProductoPositivo ):

				# Búsqueda del último id en la base de datos correspondiente.	
				ultimoId = db.session.query(func.max(Acciones.identificador)).\
								first()
				identificador  = ultimoId[0]

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				identificador = 1 if identificador == None else identificador + 1

				accionNueva = Acciones(idProducto, identificador, descripcion)
				db.session.add(accionNueva)
				db.session.commit()
				return( True )
		
		return( False )
	
	#.-------------------------------------------------------------------------.
	
	def buscarId(self, identificador):
		"""
			@brief Función que realiza la búsqueda de la acción cuyo id sea
				   "identificador".
			
			@param identificador: identificador de la acción a buscar.
			
			@return identificador de la acción buscada. Si no existe retorna None
					o si los parámetros fueron incorrectos retorna -1.
		"""
	
		# Booleano que indica si el parámetro ES del tipo correspondiente.
		idInt = type(identificador) == int
		
		if ( idInt ):
			idBuscado = db.session.query(Acciones).\
							filter(Acciones.identificador == identificador).\
							first()
			return( idBuscado )
		return( None )
	
	#.-------------------------------------------------------------------------.

	def modificar(self, identificador, descripcion):
		"""
			@brief Función que permite modificar los datos de la acción cuyo id
				   sea "identificador".
		
			@param identificador: identificador de la accion a modificar.
			@param descripcion  : nueva descripción para la acción dada.
			
			@return True si se modificó la acción dada. De lo contrario retorna
					False.
		"""
		
		# Booleanos que indican si los parámetros son del tipo correspondiente.
		idInt = type(identificador) == int
		descripcionStr = type(descripcion) == str
		
		if ( idInt and descripcionStr ):
			# Booleanos que indican si los parámetros tienen el tamaño válido.
			idPositivo 	= identificador > 0
			descripcionLongitud = 1 <= len(descripcion) <= 500
			
			if ( idPositivo and descripcionLongitud ):
				idBuscado = self.buscarId(identificador)
				
				if ( idBuscado != None ):
					db.session.query(Acciones).\
						filter(Acciones.identificador == identificador).\
						update({'descripcion':descripcion})
					db.session.commit()
					return( True )
					
		return( False )
	
	#.-------------------------------------------------------------------------.

	def eliminar(self, identificador):
		"""
			@brief Función que permite eliminar una acción cuyo id
				   sea "identificador".
			
			@return True si se eliminó la acción dada. De lo contrario retorna
					False.
		"""

		idInt = type(identificador) == int
		
		if (idInt):
			idPositivo = identificador >0
			
			if ( idPositivo ):
				
				accionBuscada = db.session.query(Acciones).\
								filter(Acciones.identificador == identificador).\
								first()

				if(accionBuscada != None):


					accionContenida = db.session.query(Historias).\
									  filter(Historias.idAccion == identificador).\
									  first()

					if ( accionContenida == None):
			
						db.session.delete(accionBuscada)
						db.session.commit()
						return ( True )
			
		return ( False )
