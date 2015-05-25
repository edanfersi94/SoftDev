# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        
"""

# Función a importar.
import model

# Numero de productos creados en la base de datos.
num_productos   = 0

# Clase que tendra las diferentes funcionalidades de la tabla "Pila".
class clsProducto():

	#-------------------------------------------------------------------------------
	
	def insert_Producto(self, newDescripProducto):
		"""
			@brief Funcion que permite insertar un nuevo producto en la base de datos.
			
			@param newDescripProducto : Descripcion del producto a insertar.

			@return Tupla que contiene un booleano y un numero.

					*(True, num_productos) si se inserta correctamente el producto.
					*(False, 0) en caso contrario.

		"""
		
		global num_productos
		salida = (False, 0)

		# Booleano que indica si el tipo es el correcto.
		descripIsStr = type(newDescripProducto) == str
	
		if ( descripIsStr ):

			# Booleano que indica si cumplen con los limites.
			descripLenValid = 1 <= len(newDescripProducto) <= 500
		
			if ( descripLenValid ):
				num_productos = num_productos + 1
				newProducto = model.Pila(num_productos, newDescripProducto)
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

	def modify_Producto(self, idProducto, newDescripProducto):
		"""
			@brief Funcion que modifica los datos del producto cuyo id sea "idProducto".
			
			@param idProducto	  	: id del producto a modificar.
			@param newDescripProducto : nueva descripcion para el producto dado.
			
			@return True si se modifico el producto dado. De lo contrario False.
		"""
		
		# Booleanos que indican si el tipo es el correcto.
		descripIsStr = type(newDescripProducto) == str
		idIsInt 	 = type(idProducto) == int
		
		if ( idIsInt and descripIsStr ):
			# Booleanos que indican si se cumplen los limites.
			idIsPositive 	= idProducto > 0
			descripLenValid = 1 <= len(newDescripProducto) <= 500
			
			if ( idIsPositive and descripLenValid ):
				query = self.find_idProducto(idProducto)
				
				if ( query != [] ):
					producto = model.Pila.idPila == idProducto
					model.db.session.query(model.Pila).filter(producto).\
						update({'descripProducto':(newDescripProducto)})
					model.db.session.commit()
					return( True )
					
		return( False )
	
	#--------------------------------------------------------------------------------	
	