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
    
    def insert_Historia(self, newCodigo, newIdProducto, newTipo):
        
        """
            @brief Funcion que permite insertar un nueva historia en la base de datos.
            
            @param newTipo : Tipos de Historia.
                   newCodigo: Codigo que le asigna a la historia de un usuario el dueño del producto
                   newIdProducto: IdProducto asociado la historia de usario

            @return Variable Booleana

                    * True cuando se inserta correctamente en la bases de datos.
                    * False caso contrario.

        """
        
        query = model.db.session.query(model.func.max(model.Historia_Usuario.idHistoria_Usuario)).all()
        
        # Se toma la tupla resultante
        tuplaResult = query[0]
        
        num_historias = int(tuplaResult[0] or 0)
        num_historias = num_historias + 1        
        

        # Booleano que indica si el tipo es el correcto.
        codigoStr = type(newCodigo) == str
        
        if (codigoStr):
            
            # Booleano que indica si cumplen con los limites.
            codigoLenValid = 1<= len(newCodigo)<=13
            
            IdProductoInt = type(newIdProducto)== int
            
            if(IdProductoInt and codigoLenValid):
                
                productoEsp = model.Pila.idPila == newIdProducto
                query_producto = model.db.session.query(model.Pila).filter(productoEsp).all()
                
                historiaEsp = model.Historia_Usuario.idHistoria_Usuario == num_historias
                query_historia = model.db.session.query(model.Historia_Usuario).filter(historiaEsp).all()
                
                if(query_producto!=[] and query_historia==[]):
                    newHistoriaUsuario = model.Historia_Usuario(num_historias,newCodigo, newIdProducto, newTipo, NewAccion)
                    model.db.session.add(newHistoriaUsuario)
                    model.db.session.commit()
                    
                    return (True)
                    
        return ( False )
    
    def find_CodHistoria(self,newcodigo):
        
        """
            @brief Funcion que realiza la busqueda de la historia cuyo identificador
                   sea "codigoHistoria_Usuario".
            
            @param newcodigo: Identificador de la historia de usuario a buscar.
            
            @return lista que contiene las tuplas obtenidas del subquery. De lo 
                    contrario retorna la lista vacia.
        """
        
        codigoStr = type(newcodigo) == str
        codigoLenValid = 1<= len(newcodigo)<=10
        
        if codigoStr and codigoLenValid:
            productoEsp = model.Pila.idPila == idProducto
            historiaEsp = model.Historia_Usuario.codigoHistoria_Usuario == newcodigo
            query = model.db.session.query(model.Historia_Usuario).filter(historiaEsp).all()
            return( query )

        return ([])

    