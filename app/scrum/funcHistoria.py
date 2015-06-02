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

# Numero de historias creadas en la base de datos.


# Clase que tendra las diferentes funcionalidades de la tabla "Historia_Usuario".

class clsHistoria():
    
    #-------------------------------------------------------------------------------
    
    def insert_Historia(self, newIdProducto, newCodigoHistoria, newTipo, newAccion):
        
        """
            @brief Funcion que permite insertar un nueva historia en la base de datos.
            
            @param newTipo : Tipos de Historia.
                   newCodigo: Codigo que le asigna a la historia de un usuario el dueño del producto
                   newIdProducto: IdProducto asociado la historia de usario

            @return Variable Booleana

                    * True cuando se inserta correctamente en la bases de datos.
                    * False caso contrario.

        """
        
        salida = (False, 0)

        # Búsqueda del identificador más alto.
        query = model.db.session.query(model.func.max(model.Historia_Usuario.idHistoria_Usuario)).all()
        
        # Se toma la tupla resultante
        tuplaResult = query[0]
        
        num_historias = tuplaResult[0]

        # Booleanos que indican si el tipo es el correcto.
        idProductoIsInt = type(newIdProducto) == int
        codigoHistoriaIsStr = type(newCodigoHistoria) == str
    

        if (codigoHistoriaIsStr and idProductoIsInt ):
            
            # Booleano que indica si cumplen con los limites.
            codigoLenValid = 1<= len(newCodigoHistoria)<=13
            
            if(codigoLenValid):
                if (num_historias == None):
                    num_historias = 0
                num_historias = num_historias + 1

                newHistoriaUsuario = model.Historia_Usuario(num_historias, newCodigoHistoria, newIdProducto, newTipo, newAccion)
                model.db.session.add(newHistoriaUsuario)
                model.db.session.commit()  
                salida = (True, num_historias)
                
        return ( salida )
 
    #-------------------------------------------------------------------------------

    def find_CodHistoria(self,newcodigo):
        
        """
            @brief Funcion que realiza la busqueda de la historia cuyo identificador
                   sea "codigoHistoria_Usuario".
            
            @param newcodigo: Identificador de la historia de usuario a buscar.
            
            @return lista que contiene las tuplas obtenidas del subquery. De lo 
                    contrario retorna la lista vacia.
        """
        
        codigoStr = type(newcodigo) == str
        
        
        if codigoStr:
            codigoLenValid = 1<= len(newcodigo)<=10
            if (codigoLenValid):
                productoEsp = model.Pila.idPila == idProducto
                historiaEsp = model.Historia_Usuario.codigoHistoria_Usuario == newcodigo
                query = model.db.session.query(model.Historia_Usuario).filter(historiaEsp).all()
                return( query )

        return ([])

    #-------------------------------------------------------------------------------

    def modify_Historia(self, idProducto, idHistoria):

        # Booleanos que indican si el tipo es correcto.
        idHistoriaIsInt = type(idHistoria) == int
        idProductoIsInt = type(idProducto) == int

        if (idHistoriaIsInt and idProductoIsInt):
            idHistoriaIsPos = idHistoria > 0
            idProductoIsPos = idProducto > 0

            if ( idHistoriaIsPos and idProductoIsPos ):
                    historiaQuery = model.Historia_Usuario.idHistoria_Usuario == idHistoria
                    productoHistoria = model.Historia_Usuario.id_Pila_Historia_Usuario = idProducto
                    query = model.db.session.query(model.Historia_Usuario).filter(historiaQuery, productoHistoria).all()
                    historiaAct = query
                    
                    model.db.session.delete(historiaAct)
                    model.db.session.commit()
                    
                    return( True )
        return( False )

    #-------------------------------------------------------------------------------
    
    def find_Historia(self,idHistoria_Usuario):
        
        idHistoriaIsInt = type(idHistoria_Usuario) == int
        
        if (idHistoriaIsInt):
            idHistoriaIsPos = idHistoria >0
            
            if (idHistoriaIsPos):
                historiaEsp  = model.Historia_Usuario.idHistoria_Usuario == idHistoria_Usuario
                query = model.db.session.query(model.Historia_Usuario).filter(historiaEsp).all()
                historia = query[0]
                    
                return (historia)
            
            return ([])
        
        return ([])
    