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
		eliminar actores de una historia.
"""

#------------------------------------------------------------------------------------------

# Funciones a importar:
from model import db, func, ActoresHistorias
from sqlalchemy.sql.dml import Insert

#----------------------------------------------------------------------------------------------

# Clase que tendra las diferentes funcionalidades de la tabla " ActoresHistorias "
class clsHistoriaActores():

	#-------------------------------------------------------------------------------

	def insertar(self, idHistoria, idActor):

		"""
			@brief Función que permite insertar un nuevo actor de una historia en la base de 
				   datos.
			
			@param idHistoria 	: identificador de la historia al que pertenecerá el 
										  actor.
			@param idActor		: identificador del actor

			@return True si se insertó correctamente la acción deseada. 
					En caso contrario retorna False.
		"""

		# Booleanos que indican si el tipo es el correcto.
		idHistoriaInt = type(idHistoria) == int
		identificadorInt = type(id) == int

		if (idHistoriaInt and idActorInt):

			# Booleanos que indican si se cumplen los límites.
			idHistoriaPositivo = idHistoria > 0
			idActorPositivo = idActor > 0

			if (idHistoriaPositivo and idActorPositivo):

				# Búsqueda del último id en la base de datos correspondiente.	
				ultimoId = db.session.query(func.max(ActoresHistorias.id)).first()
				identificador  = ultimoId[0]

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				identificador = 1 if identificador == None else identificador + 1

				actorNuevo = model.ActoresHistorias(identificador, idHistoria, idActor)
				db.session.add(actorNuevo)
				db.session.commit()
				return( True )

		return( False )

	#-------------------------------------------------------------------------------

	def eliminar(self,idHistoria,identificador):

		"""
			@brief Función que permite eliminar los datos del actor que pertenece a una historia 
					cuyo id sea "identificador".
			
			@param idHistoria   : identificador de la historia al que pertenece el 
							   	  actor.
			@param identificador : identificador del actor a modificar.
			
			@return True si se modificó la acción dada. De lo contrario retorna
					False.
		"""
		
		idHistoriaInt = type(idHistoria) == int
		idActorInt = type(idActor) == int
		
		if (idHistoriaInt and idActorInt):
			idHistoriaPositivo = idHistoria >0
			idActorPositivo  = idActor> 0
			
			if ( idHistoriaPositivo and idActorPositivo):
				actorBuscado = db.session.query(ActoresHistorias).\
						filter(ActoresHistorias.identificador == identificador, 
							   ActoresHistorias.idHistoria == idHistoria).\
						all()

				if ( actorBuscado != []):
					for actor in actorBuscado:
						db.session.delete(actor)
						db.session.commit()
					return ( True )
			
		return ( False )
	
	#-------------------------------------------------------------------------------			
	def buscarActor(self,idHistoria):

		"""
			@brief Función que realiza la busqueda del actor de una historia cuyo id sea
				   "identificador".
			
			@param idHistoria   : identificador de la historia al que pertenece el 
								  actor.
			
			@return lista que contiene las tuplas obtenidas del subquery. De lo 
					contrario retorna la lista vacia.
		"""

		listaActor = []
		
		idHistoriaInt = type(idHistoria) == int
		
		if (idHistoriaInt):
			idHistoriaPositivo = idHistoria >0
			
			if (idHistoriaPositivo):
				actorBuscado = db.session.query(ActoresHistorias).\
							filter(ActoresHistorias.idHistoria == idHistoria).\
							all()

				if(actorBuscado != []):
				
					for actor in actorBuscado:
						identificador = actor.identificador
						listaActor.append(identificador)
						
					return (listaActor)
			
			return ( -1 )
		
		return ( -1 )
					
					