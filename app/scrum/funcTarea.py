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
        eliminar tareas.
"""


#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func,Historias, Tareas, Enlaces,Categorias

#.-----------------------------------------------------------------------------.


# Clase que tendrá las diferentes funcionalidades de la tabla "Acciones".
class clsTarea():

    def insertar(self, idHistoria,descripcion, idCategoria, peso):
        
        """
            @brief Función que permite insertar los datos de la tarea cuyo id
                   sea "identificador".
        
            @param idHistoria: identificador de la historia asociada a la tarea.
            @param descripcion  : nueva descripción para la tarea dada.
            @param idCategoria  : identificador de la categoria asociada a la tarea.
            @param peso  : peso de la categoria.
            
            @return True si se inserto la tarea dada. De lo contrario retorna
                    False.
        """

        descripcionStr = type(descripcion) == str
        idHistoriaInt  = type(idHistoria)  == int
        idCategoriaInt = type(idCategoria) == int
        pesoInt = type(peso) == int
        
        categoriaBuscada = db.session.query(Categorias).\
                            filter(Categorias.identificador == idCategoria).\
                            first()
                          

        if ( descripcionStr and idHistoriaInt and idCategoriaInt and pesoInt and (categoriaBuscada !=None)):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            descripcionLongitud = 1 <= len(descripcion) <= 500
            idHistoriaPositivo  = idHistoria> 0
            idCategoriaPositivo = idCategoria >0
            pesoPositivo = peso >0


            if ( descripcionLongitud and idHistoriaPositivo and idCategoriaPositivo and pesoPositivo ):

                productoBuscado = db.session.query(Historias).\
                                    filter(Historias.identificador == idHistoria).\
                                    first()
                idProductoBuscado = productoBuscado.idProducto

                enlacesActuales = db.session.query(Enlaces).\
                                  filter(Enlaces.idProducto== idProductoBuscado).all()
                listaEnlace = {}

                for enlace in enlacesActuales:
        
                    if (enlace.idClave in listaEnlace):
                        listaEnlace[enlace.idClave] += [enlace.idValor]
    
                    else:
                        listaEnlace[enlace.idClave] = [enlace.idValor]

                    if not(enlace.idValor in listaEnlace):
                        listaEnlace[enlace.idValor] =[]

                 # Búsqueda del último id en la base de datos correspondiente.   
                ultimoId = db.session.query(func.max(Tareas.identificador)).\
                                    first()
                identificador  = ultimoId[0]

                # Si no hay acciones en la base de datos, entonces se inicializa 
                # el contador.
                identificador = 1 if identificador == None else identificador + 1
                if (listaEnlace[idHistoria] == [] ):

                    tareaNueva = Tareas(identificador, idHistoria, descripcion, idCategoria, peso)
                    db.session.add(tareaNueva)
                    db.session.commit()
                    return((True,identificador))

        
        return( (False,0) )
#.----------------------------------------------------------------------------------------        

    def modificar(self, identificador, descripcion,idCategoria, peso):
        """
            @brief Función que permite modificar los datos de la tarea cuyo id
                   sea "identificador".
        
            @param identificador: identificador de la tarea a modificar.
            @param descripcion  : nueva descripción para la tarea dada.
            @param idCategoria  : identificador de la categoria asociada a la tarea.
            @param peso  : peso de la categoria.
            
            @return True si se modificó la tarea dada. De lo contrario retorna
                    False.
        """
        
        # Booleanos que indican si los parámetros son del tipo correspondiente.
        idInt = type(identificador) == int
        descripcionStr = type(descripcion) == str
        
        if ( idInt and descripcionStr ):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            idPositivo  = identificador > 0
            descripcionLongitud = 1 <= len(descripcion) <= 500
            
            if ( idPositivo and descripcionLongitud ):
                idBuscado = db.session.query(Tareas).filter(Tareas.identificador == identificador).first()
                
                if ( idBuscado != None ):
                    db.session.query(Tareas).\
                        filter(Tareas.identificador == identificador).\
                        update({'descripcion':descripcion, 'idCategoria':idCategoria, 'peso':peso})
                    db.session.commit()
                    return( True )
                    
        return( False )

    #.-------------------------------------------------------------------------.

    def eliminar(self, identificador):
        """
            @brief Función que permite eliminar una tarea cuyo id
                   sea "identificador".
            
            @return True si se eliminó la tarea dada. De lo contrario retorna
                    False.
        """

        idInt = type(identificador) == int
        
        if (idInt):
            idPositivo = identificador >0
            
            if ( idPositivo ):
                
                tareaBuscada = db.session.query(Tareas).\
                                filter(Tareas.identificador == identificador).\
                                first()

                if(tareaBuscada != None):        
                    db.session.delete(tareaBuscada)
                    db.session.commit()
                    return ( True )
            
        return ( False )
