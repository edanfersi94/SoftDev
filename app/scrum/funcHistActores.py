# -*- coding: utf-8 -*-

# Función a importar.
import model

# Clase que tendra las diferentes funcionalidades de la tabla " ActoresHistorias "
class clsHistoriaActores():

	#-------------------------------------------------------------------------------

	def insert_Actor(self, idHistoria, idActor):

		# Búsqueda del identificador más alto.
		query = model.db.session.query(model.func.max(model.ActoresHistorias.idActoresHistoria)).all()

		# Se toma la tupla resultante.
		tuplaResult = query[0]

		num_actoresInsertado = tuplaResult[0]

		# Booleanos que indican si el tipo es el correcto.
		idHistoriaIsInt = type(idHistoria) == int
		idActoresIsInt = type(idActor) == int

		if (idHistoriaIsInt and idActoresIsInt):

			# Booleanos que indican si se cumplen los límites.
			idHistoriaIsPos = idHistoria > 0
			idActoresIsPos = idActor > 0

			if (idHistoriaIsPos and idActoresIsPos):

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				if (num_actoresInsertado == None):
					num_actoresInsertado = 0
				num_actoresInsertado = num_actoresInsertado + 1

				newActor = model.ActoresHistorias(num_actoresInsertado, idHistoria, idActor)
				model.db.session.add(newActor)
				model.db.session.commit()
				return( True )

		return( False )

		#-------------------------------------------------------------------------------

