# -*- coding: utf-8 -*-

# Función a importar.
import model

# Numero de acciones creados en la base de datos.
num_acciones   = 0

# Clase que tendra las diferentes funcionalidades de la tabla "Actores".
class clsAccion():

	#-------------------------------------------------------------------------------
	
	def insert_Accion(self, newDescripAccion):
		"""
			@brief Funcion que permite insertar una nuevo acción en la base de datos.
			
			@param newDescripAccion : Descripcion de la acción a insertar.

			@return True si se insertó la acción dada. De lo contrario False.
		"""
		
		global num_acciones

		# Booleano que indica si el tipo es el correcto.
		descripIsStr = type(newDescripAccion) == str
	
		if ( descripIsStr ):

			# Booleano que indica si cumplen con los limites.
			descripLenValid = 1 <= len(newDescripAccion) <= 500
		
			if ( descripLenValid ):
				num_acciones = num_acciones + 1
				newAccion = model.Acciones(num_acciones, newDescripAccion)
				model.db.session.add(newAccion)
				model.db.session.commit()
				return( True )
		
		return( False )
	
	#-------------------------------------------------------------------------------
	
	def find_idAccion(self, idAccion):
		"""
			@brief Funcion que realiza la busqueda de la acción cuyo identificador
				   sea "idAccion".
			
			@param idAccion: Identificador de la acción a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idAccion) == int
		
		if ( idIsInt ):
			accionesEsp = model.Acciones.idacciones == idAccion
			query = model.db.session.query(model.Acciones).filter(accionesEsp).all()
			return( query )
		return( [] )
	


	#-------------------------------------------------------------------------------

	def modify_Accion(self, idAccion, newDescripAccion):
		"""
			@brief Funcion que modifica los datos de la acción cuyo id sea "idAccion".
			
			@param idAccion	  	    : id de la accion a modificar.
			@param newDescripAccion : nueva descripcion para la acción dada.
			
			@return True si se modifico la acción dada. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		descripIsStr = type(newDescripAccion) == str
		idIsInt 	 = type(idAccion) == int
		
		if ( idIsInt and descripIsStr ):
			# Booleanos que indican si se cumplen los limites.
			idIsPositive 	= idAccion > 0
			descripLenValid = 1 <= len(newDescripAccion) <= 500
			
			if ( idIsPositive and descripLenValid ):
				query = self.find_idAccion(idAccion)
				
				if ( query != [] ):
					acciones = model.Acciones.idacciones == idAccion
					model.db.session.query(model.Acciones).filter(acciones).\
						update({'descripAcciones':(newDescripAccion)})
					model.db.session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	
	