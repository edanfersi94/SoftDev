# -*- coding: utf-8 -*-

# Función a importar.
import model


# Clase que tendra las diferentes funcionalidades de la tabla "Actores".
class clsAccion():

	#-------------------------------------------------------------------------------
	
	def insert_Accion(self, idProducto, newDescripAccion):
		"""
			@brief Funcion que permite insertar una nuevo acción en la base de datos.
			
			@param idProducto 		: Producto al que pertenecerá la acción.
			@param newDescripAccion : Descripcion de la acción a insertar.

			@return True si se insertó la acción dada. De lo contrario False.
		"""

		# Búsqueda del identificador más alto.	
		query = model.db.session.query(model.func.max(model.Acciones.idacciones)).all()
		
		# Se toma la tupla resultante
		tuplaResult = query[0]
		
		num_acciones = int(tuplaResult[0] or 0)

		# Booleano que indica si el tipo es el correcto.
		descripIsStr = type(newDescripAccion) == str
		idProdIsInt	 = type(idProducto) == int

		if ( descripIsStr and idProdIsInt ):

			# Booleano que indica si cumplen con los limites.
			descripLenValid = 1 <= len(newDescripAccion) <= 500
			idProducIsPosit = idProducto > 0

			if ( descripLenValid and idProducIsPosit ):

				# Si no hay acciones en la base de datos, entonces se inicializa el contador.
				if num_acciones == None:
					num_acciones = 0				
				num_acciones = num_acciones + 1

				newAccion = model.Acciones(idProducto, num_acciones, newDescripAccion)
				model.db.session.add(newAccion)
				model.db.session.commit()
				return( True )
		
		return( False )
	
	#-------------------------------------------------------------------------------
	
	def find_idAccion(self, idProducto, idAccion):
		"""
			@brief Funcion que realiza la busqueda de la acción cuyo identificador
				   sea "idAccion".
			
			@param idProducto : Producto al que pertenece la acción.
			@param idAccion   : Identificador de la acción a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idAccion) == int
		idProdIsInt	 = type(idProducto) == int
		
		if ( idIsInt and idProdIsInt ):
			accionesEsp = model.Acciones.idacciones == idAccion 
			idProductoEsp =  model.Acciones.idProducto == idProducto
			query = model.db.session.query(model.Acciones).filter(accionesEsp, idProductoEsp).all()
			return( query )
		return( [] )
	
	#-------------------------------------------------------------------------------

	def modify_Accion(self, idProducto, idAccion, newDescripAccion):
		"""
			@brief Funcion que modifica los datos de la acción cuyo id sea "idAccion".
			
			@param idProducto 		: Producto al que pertenece la acción.
			@param idAccion	  	    : id de la accion a modificar.
			@param newDescripAccion : nueva descripcion para la acción dada.
			
			@return True si se modifico la acción dada. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		descripIsStr = type(newDescripAccion) == str
		idIsInt 	 = type(idAccion) == int
		idProdIsInt	 = type(idProducto) == int
		
		if ( idIsInt and descripIsStr ):
			# Booleanos que indican si se cumplen los limites.
			idProducIsPosit = idProducto > 0	
			idIsPositive 	= idAccion > 0
			descripLenValid = 1 <= len(newDescripAccion) <= 500
			

			if ( idIsPositive and descripLenValid and idProducIsPosit):
				query = self.find_idAccion( idProducto, idAccion)
				
				if ( query != [] ):
					acciones = model.Acciones.idacciones == idAccion 
					idProductoEsp =  model.Acciones.idProducto == idProducto
					model.db.session.query(model.Acciones).filter(acciones, idProductoEsp).\
						update({'descripAcciones':(newDescripAccion)})
					model.db.session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	