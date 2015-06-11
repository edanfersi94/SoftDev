"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
		Módulo que contiene los métodos que permitirán insertar, modificar y
		eliminar objetivos de una historia.
"""

# Funciones a importar:
from model import db, func, ObjHistorias
from sqlalchemy.sql.dml import Insert

# Clase que tendra las diferentes funcionalidades de la tabla " ObjHistorias "
class clsHistoriaObj():

	#.-------------------------------------------------------------------------.

	def insertar(self, idHistoria, idObjetivo):
		"""
			@brief Función que permite insertar un nuevo objetivo de una historia 
				   en la base de datos.
			
			@param idHistoria: identificador de la historia al que pertenecerá el 
							   objetivo.
			@param idObjetivo: identificador del objetivo que se asociará a la 
							   historia.

			@return True si se insertó correctamente el objetivo deseada. En caso 
					contrario retorna False.
		"""

		# Booleanos que indican si el tipo es el correcto.
		idHistoriaInt = type(idHistoria) == int
		idObjetivoInt = type(idObjetivo) == int

		if (idHistoriaInt and idObjetivoInt):

			# Booleanos que indican si se cumplen los límites.
			idHistoriaPositivo = idHistoria > 0
			idObjetivoPositivo = idObjetivo > 0

			if (idHistoriaPositivo and idObjetivoPositivo):

				# Búsqueda del último id en la base de datos correspondiente.	
				ultimoId = db.session.query(func.max(ObjHistorias.identificador)).\
								first()
				identificador  = ultimoId[0]

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				identificador = 1 if identificador == None else identificador + 1

				objetivoNuevo = ObjHistorias(identificador ,idHistoria, idObjetivo)
				db.session.add(objetivoNuevo)
				db.session.commit()
				return( True )

		return( False )

	#.-------------------------------------------------------------------------.
		
	def eliminar(self, idHistoria):
		"""
			@brief Función que permite eliminar los datos del objetivo que 
				   pertenece a una historia cuyo id sea "identificador".
			
			@param idHistoria: identificador de la historia al que pertenece el/los 
							   objetivo(s).
			@return True si se modificó la acción dada. En caso contrario 
					retorna False.
		"""

		# Booleano que indica si el parámetro es del tipo correspondiente.		
		idHistoriaInt = type(idHistoria) == int
		
		if ( idHistoriaInt ):
			idHistoriaPositivo = idHistoria > 0

			if ( idHistoriaPositivo ):
				
				objetivoBuscado = db.session.query(ObjHistorias).\
								filter(ObjHistorias.idHistoria == idHistoria).\
								all()
				
				if(objetivoBuscado != []):
					for objetivo in objetivoBuscado:
						db.session.delete(objetivo)
						db.session.commit()
					return ( True )
		return ( False )
				
	#.-------------------------------------------------------------------------.