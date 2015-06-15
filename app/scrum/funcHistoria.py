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
            codigoHistoriaLongitud = 1 <= len(codigoHistoria) <= 10
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

    def modificar(self, identificador, tipo, codigo, idAccion, idSuper, idEscala):
        """
            @brief Función que elimina la historia cuyo id sea "identificador".

            @param identificador: id de la historia a modificar.
            @param tipo: entero que indica el nuevo tipo de la historia.
            @param codigo: nuevo código de la historia.
            @param idAccion: identificador de la acción a asociar ha la historia.
            @param idSuper : identificador de la historia que será la super.
            @param idEscala: entero que indica la nueva escala de la historia.
             
            @return True si la historia deseada fue eliminada correctamente. En
                    caso contrario retorna False. 
        """

        # Booleanos que indican si los parámetros son del tipo correspondiente.
        identificadorInt = type(identificador) == int
        tipoInt = type(tipo) == int
        codigoStr = type(codigo) == str
        idAccionInt = type(idAccion) == int
        idSuperInt  = type(idSuper) == int
        idEscalaInt = type(idEscala) == int 

        print(identificadorInt, tipoInt, codigoStr, idAccionInt, idSuperInt, idEscalaInt)
        if ( identificadorInt and tipoInt and codigoStr and idAccionInt and idSuperInt
             and idEscalaInt):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            identificadorPositivo = identificador > 0
            tipoLongitud = 0 < tipo < 3
            codigoLongitud = len(codigo) <= 10
            idAccionPositivo = idAccion > 0
            idSuperPositivo = idSuper >= 0
            idEscalaPositivo = idEscala > 0
            print(identificadorPositivo, tipoLongitud, codigoLongitud ,idAccionPositivo, idSuperPositivo, idEscalaPositivo)
            if ( identificadorPositivo and tipoLongitud and codigoLongitud and idAccionPositivo
                 and idSuperPositivo and idEscalaPositivo):
        
                    idBuscado = db.session.query(Historias).\
                                    filter( Historias.identificador == identificador).\
                                    first()

                    if ( idBuscado != None ):
                        
                        if( idBuscado.tipo != tipo):
                            db.session.query(Historias).\
                            filter(Historias.identificador == identificador).\
                            update({'tipo': tipo})
                            db.session.commit()
                            
                        if( idBuscado.codigo != codigo):
                            db.session.query(Historias).\
                            filter(Historias.identificador == identificador).\
                            update({'codigo': codigo})
                            db.session.commit()
                            
                        if( idBuscado.idAccion != idAccion):
                            db.session.query(Historias).\
                            filter(Historias.identificador == identificador).\
                            update({'idAccion': idAccion})
                            db.session.commit()

                        if( idBuscado.idSuper != idSuper):
                            db.session.query(Historias).\
                            filter(Historias.identificador == identificador).\
                            update({'idSuper': idSuper})
                            db.session.commit()
                            
                        if( idBuscado.idEscala != idEscala):
                            db.session.query(Historias).\
                            filter(Historias.identificador == identificador).\
                            update({'idEscala': idEscala})
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