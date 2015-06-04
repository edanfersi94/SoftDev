# -*- coding: utf-8 -*-

# Función a importar.
import model

# Clase que tendra las diferentes funcionalidades de la tabla "Pila".
class clsProducto():

	#-------------------------------------------------------------------------------
	
	def insert_Producto(self, nuevoNombre, newDescripProducto, nuevaEscala):
		"""
			@brief Funcion que permite insertar un nuevo producto en la base de datos.
			
			@param newDescripProducto : Descripcion del producto a insertar.

			@return Tupla que contiene un booleano y un numero.

					*(True, num_productos) si se inserta correctamente el producto.
					*(False, 0) en caso contrario.

		"""

		# Búsqueda del identificador más alto.	
		query = model.db.session.query(model.func.max(model.Pila.idPila)).all()
		
		# Se toma la tupla resultante
		tuplaResult = query[0]
		
		num_productos = tuplaResult[0]

		salida = (False, 0)

		# Booleano que indica si el tipo es el correcto.
		descripIsStr = type(newDescripProducto) == str
		nombreIsStr = type(nuevoNombre) == str
		escalaIsInt = type(nuevaEscala) == int

		if ( descripIsStr and nombreIsStr and escalaIsInt ):

			# Booleano que indica si cumplen con los limites.
			descripLenValid = 1 <= len(newDescripProducto) <= 500
			nombreLenValid = 1 <= len(nuevoNombre) <= 50
			escalaLenValid = 0 < nuevaEscala < 3

			if ( descripLenValid and nombreLenValid and escalaLenValid):

				queryNombre = model.db.session.query(model.Pila).\
								filter(model.Pila.nombreProducto == nuevoNombre).\
								all()

				if (queryNombre == []):
					# Si no hay productos en la base de datos, entonces se inicializa el contador.
					if num_productos == None:
						num_productos = 0
						
					num_productos = num_productos + 1
					newProducto = model.Pila(num_productos, nuevoNombre, newDescripProducto, nuevaEscala)
					model.db.session.add(newProducto)
					model.db.session.commit()
					salida = (True, num_productos)
		
		return( salida )
	
	#-------------------------------------------------------------------------------
	
	def find_idProducto(self, idProducto):
		"""
			@brief Funcion que realiza la busqueda del producto cuyo identificador
				   sea "idProducto".
			
			@param idProducto: Identificador del producto a buscar.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""
		
		idIsInt = type(idProducto) == int
		
		if ( idIsInt ):
			productoEsp = model.Pila.idPila == idProducto
			query = model.db.session.query(model.Pila).filter(productoEsp).all()
			return( query )
		return( [] )
	


	#-------------------------------------------------------------------------------

	def modify_Producto(self, idProducto, nuevoNombre, newDescripProducto, nuevaEscala):
		"""
			@brief Funcion que modifica los datos del producto cuyo id sea "idProducto".
			
			@param idProducto	  	: id del producto a modificar.
			@param newDescripProducto : nueva descripcion para el producto dado.
			
			@return True si se modifico el producto dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		nombreIsStr  = type(nuevoNombre) == str
		descripIsStr = type(newDescripProducto) == str
		idIsInt 	 = type(idProducto) == int
		escalaIsInt  = type(nuevaEscala) == int 
		
		if ( idIsInt and descripIsStr and nombreIsStr and escalaIsInt):
			# Booleanos que indican si se cumplen los limites.
			idIsPositive 	= idProducto > 0
			descripLenValid = 1 <= len(newDescripProducto) <= 500
			nombreLenValid  = 1 <= len(nuevoNombre) <= 50
			escalaLenValid  = 0 < nuevaEscala < 3

			if ( idIsPositive and descripLenValid and nombreLenValid and escalaLenValid):
	
				queryHistoria = model.db.session.query(model.Historia_Usuario).\
									filter(model.Historia_Usuario.id_Pila_Historia_Usuario == idProducto).\
									all()
				
				query = self.find_idProducto(idProducto)

				if ((query[0].escalaProducto == nuevaEscala ) or (query[0].escalaProducto != nuevaEscala and queryHistoria == [])):
					
					queryNombre = model.db.session.query(model.Pila).\
									filter(model.Pila.nombreProducto == nuevoNombre, model.Pila.idPila == idProducto).\
									all()

					if ( query != [] and queryNombre == [] ):
						producto = model.Pila.idPila == idProducto
						model.db.session.query(model.Pila).filter(producto).\
							update({'nombreProducto': nuevoNombre,'descripProducto':(newDescripProducto), 'escalaProducto':nuevaEscala})
						model.db.session.commit()
				
						return( True )
					elif (queryNombre != [] and query[0].nombreProducto == nuevoNombre):
						producto = model.Pila.idPila == idProducto
						model.db.session.query(model.Pila).filter(producto).\
							update({'descripProducto':(newDescripProducto), 'escalaProducto':nuevaEscala})
						model.db.session.commit()
						return (True)
						
		return( False )
	
	#--------------------------------------------------------------------------------	