# -*- coding: utf-8 -*-

# Función a importar.
import model

# Clase que tendra las diferentes funcionalidades de la tabla "Objetivo".
class clsObjetivo():

	#-------------------------------------------------------------------------------
	
	def insert_Objetivo(self, idProducto, newDescripObjetivo):
		"""
			@brief Funcion que permite insertar un nuevo objetivo en la base de datos.
			
			@param idProducto 		  : Producto al que pertenecerá el objetivo.			
			@param newDescripObjetivo : Descripcion del objetivo a insertar.
			
			@return True si se insertó el objetivo dado. De lo contrario False.
		"""

		# Búsqueda del identificador más alto.		
		query = model.db.session.query(model.func.max(model.Objetivo.idObjetivo)).all()
		
		# Se toma la tupla resultante.
		tuplaResult = query[0]
		
		num_objetivos = tuplaResult[0]

		# Booleano que indica si el tipo es el correcto.
		descripIsStr = type(newDescripObjetivo) == str
		idProdIsInt	 = type(idProducto) == int
	
		if ( descripIsStr and idProdIsInt):

			# Booleano que indica si cumplen con los limites.
			descripLenValid = 1 <= len(newDescripObjetivo) <= 500
			idProducIsPosit = idProducto > 0
		
			if ( descripLenValid and idProducIsPosit ):
				
				# Si no hay objetivos en la base de datos, entonces se inicializa el contador.
				if num_objetivos == None:
					num_objetivos = 0
				
				num_objetivos = num_objetivos + 1
				newObjetivo = model.Objetivo(idProducto, num_objetivos, newDescripObjetivo)
				model.db.session.add(newObjetivo)
				model.db.session.commit()
				return( True )
		
		return( False )
	
	#-------------------------------------------------------------------------------
	
	def find_idObjetivo(self, idProducto, idObjetivo):
		"""
			@brief Funcion que realiza la busqueda del objetivo cuyo identificador
				   sea "idObjetivo".
			
			@param idProducto : Producto al que pertenece el objetivo.
			@param idObjetivo : Identificador del objetivo a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idObjetivo) == int
		idProdIsInt	 = type(idProducto) == int
		
		if ( idIsInt and idProdIsInt ):
			objetivoEsp = model.Objetivo.idObjetivo == idObjetivo 
			idProductoEsp =  model.Objetivo.idProducto == idProducto
			query = model.db.session.query(model.Objetivo).filter(objetivoEsp, idProductoEsp).all()
			return( query )
		return( [] )
	
	#-------------------------------------------------------------------------------

	def modify_Objetivo(self, idProducto, idObjetivo, newDescripObjetivo):
		"""
			@brief Funcion que modifica los datos del objetivo cuyo id sea "idObjetivo".
	
			@param idProducto 		  : Producto al que pertenece el objetivo.			
			@param idObjetivo	  	  : id del objetivo a modificar.
			@param newDescripObjetivo : nueva descripcion para el objetivo dada.
			
			@return True si se modifico el objetivo dada. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		descripIsStr = type(newDescripObjetivo) == str
		idIsInt 	 = type(idObjetivo) == int
		idProdIsInt	 = type(idProducto) == int
		
		if ( idIsInt and descripIsStr and idProdIsInt):
			# Booleanos que indican si se cumplen los limites.
			idIsPositive 	= idObjetivo > 0
			idProducIsPosit = idProducto > 0
			descripLenValid = 1 <= len(newDescripObjetivo) <= 500
			
			if ( idIsPositive and descripLenValid and idProducIsPosit):
				query = self.find_idObjetivo( idProducto, idObjetivo)
				
				if ( query != [] ):
					objetivo = model.Objetivo.idObjetivo == idObjetivo 
					idProductoEsp = model.Objetivo.idProducto == idProducto
					model.db.session.query(model.Objetivo).filter(objetivo, idProductoEsp).\
						update({'descripObjetivo':(newDescripObjetivo)})
					model.db.session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	