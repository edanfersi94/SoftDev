import model

class clsEnlace():

	def insert_Enlace(self, idProductoActual, idSuper):
		query = model.db.session.query(model.Enlaces).all()
		queryNumEnlaces = model.db.session.query(model.func.max(model.Enlaces.id_enlace)).all()
		queryNumHistorias = model.db.session.query(model.func.max(model.Historia_Usuario.idHistoria_Usuario)).all()

		idProductoIsInt = type(idProductoActual) == int
		idSuperIsInt = type(idSuper) == int  
		salida = False
		
		if (idProductoIsInt and idSuperIsInt):
			
			producto = model.db.session.query(model.Pila.idPila).filter(model.Pila.idPila == idProductoActual).all()

			idProducto= [int(i[0]) for i in producto]

			idProductoIsEsta = idProductoActual in idProducto
			
			if (idProductoIsEsta):		
				tuplaResult = queryNumHistorias[0]
				idHistoria = tuplaResult[0]
		
				if (idHistoria == None):
					idHistoria = 0
				idHistoria += 1
		
				tuplaResult = queryNumEnlaces[0]
				num_enlaces = tuplaResult[0]
		
				if (num_enlaces == None):
					num_enlaces = 0
				num_enlaces += 1
		
				listaEnlace = {}
				salida = False
				# Se genera la lista.
				for elem in query:
					if (elem.id_clave in listaEnlace):
						listaEnlace[elem.id_clave] += [elem.id_valor]
						if not(elem.id_valor in listaEnlace):
		 						listaEnlace[elem.id_valor] =[] 
					else:
						listaEnlace[elem.id_clave] = [elem.id_valor]
						if not(elem.id_valor in listaEnlace):
		 						listaEnlace[elem.id_valor] =[]
		
					if not(elem.id_valor in listaEnlace):
						listaEnlace[elem.id_valor] =[]
				print(listaEnlace)
		
				target = {}
				for key in listaEnlace:
					print(key)
					if key == idSuper:
						target[key] = listaEnlace[key] + [idHistoria]
					else:
						target[key] = listaEnlace[key]
		
				if not(idSuper in target):
					target[idSuper] = [idHistoria]
		
				print(idHistoria)
				target[idHistoria] = []
				print(target)
		
				existCiclo = self.existenciaCiclo(target)
		
				if not(existCiclo):
					newEnlace = model.Enlaces(num_enlaces, idProductoActual, idSuper, idHistoria)
					model.db.session.add(newEnlace)
					model.db.session.commit()
					salida = True
		return(salida)

   #-------------------------------------------------------------------------------

	def modify_Enlace(self, idProductoActual, viejoSuper, newSuper, idValor):

 		query = model.db.session.query(model.Enlaces).all()

 		listaEnlace = {}
 		salida = False
 		
 		idProductIsInt = type(idProductoActual) == int
 		idviejoSuperIsInt = type(viejoSuper) == int
 		idnuevoSuperIsInt = type(newSuper) == int
 		idValorIsInt = type(idValor) == int
 		
 		if (idProductIsInt and idviejoSuperIsInt and idnuevoSuperIsInt and idValorIsInt):
 			
 			producto = model.db.session.query(model.Pila.idPila).filter(model.Pila.idPila == idProductoActual).all()
 			idProducto= [int(i[0]) for i in producto]
 			idProductoIsEsta = idProductoActual in idProducto
 			
 			superv = model.db.session.query(model.Enlaces.id_enlace).filter(model.Enlaces.id_enlace == viejoSuper).all()
 			idsuperv= [int(i[0]) for i in superv]
 			idsupervEsta = viejoSuper in idsuperv
 			
 			if (idProductoIsEsta and idsupervEsta):

		 		# Se genera la lista.
		 		for elem in query:
		 			if (elem.id_clave != viejoSuper or (elem.id_clave == viejoSuper and elem.id_valor != idValor)):
		 				if (elem.id_clave in listaEnlace):
		 					listaEnlace[elem.id_clave] += [elem.id_valor]
		 					if not(elem.id_valor in listaEnlace):
		 						listaEnlace[elem.id_valor] =[] 
		 				else:
		 					listaEnlace[elem.id_clave] = [elem.id_valor]
		 					if not(elem.id_valor in listaEnlace):
		 						listaEnlace[elem.id_valor] =[]
		 			elif(elem.id_clave == viejoSuper and elem.id_valor == idValor):
		 				listaEnlace[viejoSuper] = []
		
		 			if not(elem.id_valor in listaEnlace):
		 				listaEnlace[elem.id_valor] =[]
		
		 		print(listaEnlace)
		 		target = {}
		 		for key in listaEnlace:
		 			print(key)
		 			if key == newSuper:
		 				target[key] = listaEnlace[key] + [idValor]
		 			else:
		 				target[key] = listaEnlace[key]
		
		 		target[newSuper] = [idValor]
		 		print(target)
		 		existCiclo = self.existenciaCiclo(target)
		 		print(existCiclo)
		 		if not(existCiclo):
		 			model.db.session.query(model.Enlaces).\
		 				filter(model.Enlaces.id_clave == viejoSuper,model.Enlaces.id_valor == idValor).\
		 				update({'id_clave':(newSuper)})
		 			model.db.session.commit()
		 			salida = True

 		return(salida)  	

   #-------------------------------------------------------------------------------

	def existenciaCiclo(self,G):
		color = { u : "blanco" for u in G  } 
		encontrarCiclo = [False]

		for u in G:
			if color[u] == "blanco":
				self.dfs_visit(G, u, color, encontrarCiclo)
			if encontrarCiclo[0]:
				break
		return encontrarCiclo[0]
     
    #-------

	def dfs_visit(self,G, u, color, encontrarCiclo):
		if encontrarCiclo[0]:                         
			return
		color[u] = "gris"
		for v in G[u]:
			if color[v] == "gris":                 
				encontrarCiclo[0] = True       
				return
			if color[v] == "blanco":                 
				self.dfs_visit(G, v, color, encontrarCiclo)
		color[u] = "negro"                         

    #-------------------------------------------------------------------------------


    #-------------------------------------------------------------------------------