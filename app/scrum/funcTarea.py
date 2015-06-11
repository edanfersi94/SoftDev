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
from model import db, func,Historias, Tareas, Enlaces

#.-----------------------------------------------------------------------------.


# Clase que tendrá las diferentes funcionalidades de la tabla "Acciones".
class clsTarea():

    def insertar(self, idHistoria,descripcion):

        descripcionStr = type(descripcion) == str
        idHistoriaInt  = type(idHistoria)  == int

        if ( descripcionStr and idHistoriaInt ):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            descripcionLongitud = 1 <= len(descripcion) <= 500
            idHistoriaPositivo  = idHistoria> 0


            if ( descripcionLongitud and idHistoriaPositivo ):

                # Búsqueda del último id en la base de datos correspondiente.   
                ultimoId = db.session.query(func.max(Tareas.identificador)).\
                                first()
                identificador  = ultimoId[0]

                hoja = db.session.query(Historias).\
                        filter(Historias.identificador == idHistoria).\
                        first()
                if (hoja.idSuper == 0):

                    # Si no hay acciones en la base de datos, entonces se inicializa 
                    # el contador.
                    identificador = 1 if identificador == None else identificador + 1

                    tareaNueva = Tareas(identificador, idHistoria, descripcion)
                    db.session.add(tareaNueva)
                    db.session.commit()
                    return((True,identificador))

        
        return( (False,0) )
#.----------------------------------------------------------------------------------------        

    def modificar(self, identificador, descripcion):
        """
            @brief Función que permite modificar los datos de la acción cuyo id
                   sea "identificador".
        
            @param identificador: identificador de la tarea a modificar.
            @param descripcion  : nueva descripción para la tarea dada.
            
            @return True si se modificó la acción dada. De lo contrario retorna
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
                        update({'descripcion':descripcion})
                    db.session.commit()
                    return( True )
                    
        return( False )

    #.-------------------------------------------------------------------------.

    def eliminar(self, identificador):
        """
            @brief Función que permite eliminar una acción cuyo id
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
