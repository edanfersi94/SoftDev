# -*- coding: utf-8 -*-

# Función a importar.
import model
from pickle import APPEND

# Clase que tendra las diferentes funcionalidades de la tabla " ObjHistorias "
class clsHistoriaObj():

	#-------------------------------------------------------------------------------

	def insert_Objetivo(self, idHistoria, idObjetivo):

		# Búsqueda del identificador más alto.
		query = model.db.session.query(model.func.max(model.ObjHistorias.idObjetivoHistoria)).all()

		# Se toma la tupla resultante.
		tuplaResult = query[0]

		num_objInsertado = tuplaResult[0]

		# Booleanos que indican si el tipo es el correcto.
		idHistoriaIsInt = type(idHistoria) == int
		idObjetivoIsInt = type(idObjetivo) == int

		if (idHistoriaIsInt and idObjetivoIsInt):

			# Booleanos que indican si se cumplen los límites.
			idHistoriaIsPos = idHistoria > 0
			idObjetivoIsPos = idObjetivo > 0

			if (idHistoriaIsPos and idObjetivoIsPos):

				# Si no hay acciones en la base de datos, entonces se inicializa 
				# el contador.
				if (num_objInsertado == None):
					num_objInsertado = 0
				num_objInsertado = num_objInsertado + 1

				newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
				model.db.session.add(newObj)
				model.db.session.commit()
				return( True )

		return( False )

		#-------------------------------------------------------------------------------
		
	def modify_Objetivo(self,idHistoria,idObjetivo):
		
		idHistoriaIsInt = type(idHistoria) == int
		idObjetivoIsInt = type(idObjetivo) == int
		
		if (idHistoriaIsInt and idObjetivoIsInt):
			idHistoriaIsPos = idHistoria >0
			idObjetivoIsPos = idObjetivo> 0
			
			if (idHistoriaIsPos and idObjetivoIsPos):
				objEsp   = model.ObjHistorias.idObjetivo == idObjetivo
				historiaEsp  = model.ObjHistorias.idHistoria == idHistoria
				query = model.db.session.query(model.ObjHistorias).filter(objEsp, historiaEsp).all()
				objetivo = query[0]

				model.db.session.delete(objetivo)
				model.db.session.commit()
				
				return ( True )
			
		return ( False )
				
				
	def find_Objetivo(self,idHistoria):
		listaObjetivo = []
		
		idHistoriaIsInt = type(idHistoria) == int
		
		if (idHistoriaIsInt):
			idHistoriaIsPos = idHistoria >0
			
			if (idHistoriaIsPos):
				historiaEsp  = model.ObjHistorias.idHistoria == idHistoria
				query = model.db.session.query(model.ObjHistorias).filter(historiaEsp).all()
				objetivo = query
				
				for obj in objetivo:
					idObjetivo = obj.idObjetivo
					listaObjetivo.append(idObjetivo)
					
				return (listaObjetivo)
			
			return ([])
		
		return ([])		
			
					