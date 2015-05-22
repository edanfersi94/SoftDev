# -*- coding: utf-8 -*-

# Función a importar.
import model

# Numero de objetivos creados en la base de datos.
num_objetivos   = 0

# Clase que tendra las diferentes funcionalidades de la tabla "Objetivo".
class clsObjetivo():

	#-------------------------------------------------------------------------------
	
	def insert_Objetivo(self, newDescripObjetivo):
		"""
			@brief Funcion que permite insertar un nuevo objetivo en la base de datos.
			
			@param newDescripObjetivo : Descripcion del objetivo a insertar.

			@return True si se insertó el objetivo dado. De lo contrario False.
		"""
		
		global num_objetivos

		# Booleano que indica si el tipo es el correcto.
		descripIsStr = type(newDescripObjetivo) == str
	
		if ( descripIsStr ):

			# Booleano que indica si cumplen con los limites.
			descripLenValid = 1 <= len(newDescripObjetivo) <= 500
		
			if ( descripLenValid ):
				num_objetivos = num_objetivos + 1
				newObjetivo = model.Objetivo(num_objetivos, newDescripObjetivo)
				model.db.session.add(newObjetivo)
				model.db.session.commit()
				return( True )
		
		return( False )
	
	#-------------------------------------------------------------------------------
	
	def find_idObjetivo(self, idObjetivo):
		"""
			@brief Funcion que realiza la busqueda del objetivo cuyo identificador
				   sea "idObjetivo".
			
			@param idObjetivo: Identificador del objetivo a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idObjetivo) == int
		
		if ( idIsInt ):
			objetivoEsp = model.Objetivo.idObjetivo == idObjetivo
			query = model.db.session.query(model.Objetivo).filter(objetivoEsp).all()
			return( query )
		return( [] )
	


	#-------------------------------------------------------------------------------

	def modify_Objetivo(self, idObjetivo, newDescripObjetivo):
		"""
			@brief Funcion que modifica los datos del objetivo cuyo id sea "idObjetivo".
			
			@param idObjetivo	  	  : id del objetivo a modificar.
			@param newDescripObjetivo : nueva descripcion para el objetivo dada.
			
			@return True si se modifico el objetivo dada. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		descripIsStr = type(newDescripObjetivo) == str
		idIsInt 	 = type(idObjetivo) == int
		
		if ( idIsInt and descripIsStr ):
			# Booleanos que indican si se cumplen los limites.
			idIsPositive 	= idObjetivo > 0
			descripLenValid = 1 <= len(newDescripObjetivo) <= 500
			
			if ( idIsPositive and descripLenValid ):
				query = self.find_idObjetivo(idObjetivo)
				
				if ( query != [] ):
					objetivo = model.Objetivo.idObjetivo == idObjetivo
					model.db.session.query(model.Objetivo).filter(objetivo).\
						update({'descripObjetivo':(newDescripObjetivo)})
					model.db.session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	
	