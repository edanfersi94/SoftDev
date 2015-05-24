# -*- coding: utf-8 -*-

# Función a importar.
import model

# Numero de actores creados en la base de datos.
num_actores   = 0

# Clase que tendra las diferentes funcionalidades de la tabla "Actores".
class clsActor():

	#-------------------------------------------------------------------------------
	
	def insert_Actor(self, idProducto, newNameActor,newDescripActor):
		"""
			@brief Funcion que permite insertar un nuevo actor en la base de datos.

			@param idProducto 		: Producto al que pertenecerá el actor.						
			@param newNameActor 	: Nombre del actor a insertar.
			@param newDescripActor 	: Descripcion del actor a insertar.

			@return True si se inserto el actor dado. De lo contrario False.
		"""

		global num_actores

		# Booleanos que indican si el tipo es el correcto.
		descripIsStr = type(newDescripActor) == str
		nameIsStr = type(newNameActor) == str
		idProdIsInt	 = type(idProducto) == int

		if ( nameIsStr and descripIsStr and idProdIsInt ):

			# Booleanos que indican si cumplen con los limites.
			nameLenValid = 1 <= len(newNameActor) <= 50
			descripLenValid = 1 <= len(newDescripActor) <= 500
			idProducIsPosit = idProducto > 0
		
			if (nameLenValid and descripLenValid and idProducIsPosit):
				query = self.find_nameActor( idProducto, newNameActor)

				if ( query == [] ):
					num_actores = num_actores + 1
					newActor = model.Actores(idProducto, num_actores,newNameActor, newDescripActor)
					model.db.session.add(newActor)
					model.db.session.commit()
					return( True )
		
		return( False )
		
	#-------------------------------------------------------------------------------
	
	def find_idActor(self, idProducto, idActor):
		"""
			@brief Funcion que realiza la busqueda del actor cuyo identificador
				   sea "idActor".

			@param idProducto : Producto al que pertenece el actor.			
			@param idActor: Identificador del actor a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idActor) == int
		idProdIsInt	 = type(idProducto) == int		

		if ( idIsInt and idProdIsInt ):
			actoresEsp = model.Actores.id_actores == idActor
			idProductoEsp =  model.Actores.idProducto == idProducto
			query = model.db.session.query(model.Actores).filter(actoresEsp, idProductoEsp).all()
			return( query )
		return( [] )
	
	#-------------------------------------------------------------------------------

	def find_nameActor(self, idProducto, nameActor):
		"""
			@brief Funcion que realiza la busqueda de los actores cuyo identificador
				   sea "nameActor".
	
			@param idProducto : Producto al que pertenece el actor.				   
			@param nameActor  : Nombre del actor a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""

		nameIsStr = type(nameActor) == str
		idProdIsInt	 = type(idProducto) == int
		
		if ( nameIsStr and idProdIsInt ):
			actoresEsp = model.Actores.nombre_actores == nameActor
			idProductoEsp =  model.Actores.idProducto == idProducto
			query = model.db.session.query(model.Actores).filter(actoresEsp, idProductoEsp).all()
			return( query )
		return( [] )
		
	#-------------------------------------------------------------------------------

	def modify_Actor(self, idProducto, idActor, newNameActor, newDescripActor):
		"""
			@brief Funcion que modifica los datos del actor cuyo id sea "idActor".

			@param idProducto 		: Producto al que pertenece el actor.				
			@param idActor	  	    : id del actor a modificar.
			@param newNameActor 	: nuevo nombre para el actor dado.
			@param newDescripActor  : nueva descripcion para el actor dado.
			
			@return True si se modifico el actor dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		nameIsStr 	 = type(newNameActor) == str
		descripIsStr = type(newDescripActor) == str
		idIsInt 	 = type(idActor) == int
		idProdIsInt	 = type(idProducto) == int
		
		if ( nameIsStr and  idIsInt and descripIsStr and idProdIsInt ):
			# Booleanos que indican si se cumplen los limites.
			nameLenValid 	= 1 <= len(newNameActor) <= 50
			idIsPositive 	= idActor > 0
			idProducIsPosit = idProducto > 0
			descripLenValid = 1 <= len(newDescripActor) <= 500
			
			if ( nameLenValid and idIsPositive and descripLenValid and idProducIsPosit):
				query1 = self.find_idActor(idProducto, idActor)
				query2 = self.find_nameActor(idProducto, newNameActor)
				
				if (( query1 != [] ) and ( query2 == [])):
					actores = model.Actores.id_actores == idActor
					idProductoEsp =  model.Actores.idProducto == idProducto
					model.db.session.query(model.Actores).filter(actores, idProductoEsp).\
						update({'nombre_actores':(newNameActor),'descripcion_actores':(newDescripActor)})
					model.db.session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	
	