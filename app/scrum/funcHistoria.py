# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION:
        Módulo que contiene los métodos que permitirán insertar y modificar
        historias.
"""

# Funciones a importar:
from model import db, func, Historias

#.-----------------------------------------------------------------------------.

# Clase que tendra las diferentes funcionalidades de la tabla "Historias".
class clsHistoria():
    
    #.-------------------------------------------------------------------------.
    
    def insertar(self, idProducto, codigoHistoria, tipo, idAccion, idEpica, 
                 idEscala):       
        """
            @brief Funcion que permite insertar una nueva historia en la base 
                   de datos.
            
            @param idProducto: identificador del producto en donde se creará la 
                               historia.
            @param codigoHistoria: string que representará la historia.
            @param tipo: identificador que representará el tipo de la historia.
            @param idAccion: identificador de la acción a elegir.
            @param idEpica : identificador de la historia que será la épica.
            @param idEscala: identificador de la prioridad de la historia.

            @return Tupla que contiene un booleano y un numero.

                    *(True, num_productos) si se inserta correctamente el producto.
                    *(False, 0) en caso contrario.
        """

        # Booleanos que indican si los parámetros son del tipo correspondiente.
        idProductoInt = type(idProducto) == int
        codigoHistoriaStr = type(codigoHistoria) == str
        tipoInt = type(tipo) == int
        idAccionInt = type(idAccion) == int
        idEpicaInt  = type(idEpica)  == int
        idEscalaInt = type(idEscala) == int

        if ( idProductoInt and codigoHistoriaStr and tipoInt and idEpicaInt
             and idEscalaInt ):
            
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            idProductoPositivo = idProducto > 0
            codigoHistoriaLongitud = 1 <= len(codigoHistoria) <= 13
            tipoPositivo = 0 < tipo < 3
            idAccionPositivo = idAccion > 0
            idEpicaPositivo  = idEpica  >= 0
            idEscalaPositivo = idEscala > 0


            if( idProductoPositivo and codigoHistoriaLongitud and tipoPositivo 
                and idAccionPositivo and idEpicaPositivo and idEscalaPositivo ):
                
                # Búsqueda del último id en la base de datos correspondiente.   
                ultimoId = db.session.query(func.max(Historias.identificador)).\
                                first()
                identificador  = ultimoId[0]

                # Si no hay historias en la base de datos, entonces se inicializa 
                # el contador.
                identificador = 1 if identificador == None else identificador + 1

                historiaNueva = Historias(identificador, codigoHistoria, idProducto,
                                          tipo, idAccion, idEpica, idEscala)
                db.session.add(historiaNueva)
                db.session.commit()  
                return( (True, identificador) )
        return ( (False, 0) )
 
    #-------------------------------------------------------------------------------

    def eliminar(self, identificador):
        """
            @brief Función que elimina la historia cuyo id sea "identificador".

            @param identificador: id de la historia a eliminar.
            
            @return True si la historia deseada fue eliminada correctamente. En
                    caso contrario retorna False. 
        """

        # Booleano que indica si el parámetro es del tipo correspondiente.
        identificadorInt = type(identificador) == int

        if ( identificadorInt ):
            # Booleano que indica si el parámetro tiene el tamaño válido.
            identificadorPositivo = identificador > 0

            if ( identificadorPositivo ):
        
                    idBuscado = db.session.query(Historias).\
                                    filter( Historias.identificador == identificador).\
                                    first()

                    if ( idBuscado != None ):
                        db.session.delete(idBuscado)
                        db.session.commit()
                        return( True )
        return( False )

    #-------------------------------------------------------------------------------
    
    def buscarHistoria(self, identificador):
        """ 
            @brief Función que realiza la búsqueda de la historia cuyo id sea 
                   "identificador".

            @param identificador: identificador de la historia a buscar.

            @return tupla que contiene los elementos de la búsqueda deseada. 
                    En caso de no existir o el parámetro fue incorrecto retorna 
                    None.
        """

        identificadorInt = type(identificador) == int
        
        if (identificadorInt):
            identificadorPositivo = identificador > 0
            
            if (identificadorPositivo):
                historiaBuscada = db.session.query(Historias).\
                                    filter(Historias.identificador == identificador).\
                                    all()
                return (historiaBuscada)
            return ( None )
    
    #.-------------------------------------------------------------------------.
    #.-------------------------------------------------------------------------.

    def cambiarPrioridad(self, identificador, prioridad):
        """
            @brief Funcion que modifica la escala de una historia cuyo id sea 
                   "identificador" por "nuevaPrioridad".
    
            @param identificador : id de la historia ha actualizar       
            @param prioridad: nuevo valor de escala ha asignar.
            
            @return True si se modifico correctamente la prioridad de la 
                    historia deseada. En caso contrario retorna False.
        """
        
        # Booleanos que indican si los parámetros son del tipo correspondiente.
        identificadorInt  = type(identificador)  == int
        prioridadInt = type(prioridad) == int
        
        if ( identificadorInt and prioridadInt ):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            identificadorPositivo  = identificador  > 0
            prioridadPositivo = prioridad > 0

            if ( identificadorPositivo and prioridadPositivo ):

                historiaBuscada = self.buscarHistoria(identificador)
                    
                if ( historiaBuscada != None and historiaBuscada !=[]):
        
                    db.session.query(Historias).\
                        filter(Historias.identificador == identificador).\
                        update({'idEscala': prioridad})
                    db.session.commit()
                    return( True )    
        return( False )

    #.-------------------------------------------------------------------------.