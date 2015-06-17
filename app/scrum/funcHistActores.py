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

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func, ActoresHistorias
from sqlalchemy.sql.dml import Insert

#.-----------------------------------------------------------------------------.

# Clase que tendra las diferentes funcionalidades de la tabla " ActoresHistorias "
class clsHistoriaActores():

    #.-------------------------------------------------------------------------.

    def insertar(self, idHistoria, idActor):
        """
            @brief Función que permite insertar un nuevo actor de una historia 
                   en la base de datos.
            
            @param idHistoria: identificador de la historia al que pertenecerá el 
                               actor.
            @param idActor: identificador del actor que se asociará a la historia.

            @return True si se insertó correctamente la acción deseada. En caso 
                    contrario retorna False.
        """

        # Booleanos que indican si los parámetros son del tipo correspondiente.
        idHistoriaInt = type(idHistoria) == int
        idActorInt = type(idActor) == int

        if (idHistoriaInt and idActorInt):

            # Booleanos que indican si se cumplen los límites.
            idHistoriaPositivo = idHistoria > 0
            idActorPositivo = idActor > 0

            if (idHistoriaPositivo and idActorPositivo):

                # Búsqueda del último id en la base de datos correspondiente.   
                ultimoId = db.session.query(func.max(ActoresHistorias.identificador)).\
                                first()
                identificador  = ultimoId[0]

                # Si no hay acciones en la base de datos, entonces se inicializa 
                # el contador.
                identificador = 1 if identificador == None else identificador + 1

                actorNuevo = ActoresHistorias(identificador, idHistoria, 
                                                    idActor)
                db.session.add(actorNuevo)
                db.session.commit()
                return( True )

        return( False )

    #.-------------------------------------------------------------------------.

    def eliminar(self, idHistoria):
        """
            @brief Función que permite eliminar los datos del actor que pertenece 
                    a una historia cuyo id sea "idHistoria".
            
            @param idHistoria: identificador de la historia al que pertenece el/los 
                               actor(es).
            @return True si se modificó la acción dada. En caso contrario 
                    retorna False.
        """
        
        # Booleano que indica si el parámetro es del tipo correspondiente.
        idHistoriaInt = type(idHistoria) == int
        
        if (idHistoriaInt):
            # Booleano que indica si se cumplen los límites.
            idHistoriaPositivo = idHistoria > 0         
            
            if ( idHistoriaPositivo ):
                actorBuscado = db.session.query(ActoresHistorias).\
                       filter(ActoresHistorias.idHistoria == idHistoria).\
                       all()
                        
                        
                if ( actorBuscado != []):
                    for actor in actorBuscado:
                        db.session.delete(actor)
                        db.session.commit()
                    return ( True )
        return ( False )
    
    #.-------------------------------------------------------------------------.