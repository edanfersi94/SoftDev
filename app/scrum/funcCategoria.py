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
        eliminar categorias.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func, Categorias

#.-----------------------------------------------------------------------------.


# Clase que tendrá las diferentes funcionalidades de la tabla "Acciones".
class clsCategoria():

    def insertar(self,nombre, peso):
        
        """
            @brief Función que permite insertar los datos de la categoria cuyo id
                   sea "identificador".
        
            @param nombre: nombre de la categoria a insertar.
            @param peso  : peso de la categoria.
            
            @return True si se inserto la tarea dada. De lo contrario retorna
                    False.
        """

        nombreStr = type(nombre) == str
        pesoInt = type(peso) == int
        

        if ( nombreStr and pesoInt):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            nombreLongitud = 1 <= len(descripcion) <= 100
            pesoPositivo = peso >0


            if ( nombreLongitud and pesoPositivo ):
                  # Búsqueda del último id en la base de datos correspondiente.   
                ultimoId = db.session.query(func.max(Categorias.identificador)).\
                                    first()
                identificador  = ultimoId[0]

                # Si no hay acciones en la base de datos, entonces se inicializa 
                # el contador.
                identificador = 1 if identificador == None else identificador + 1


                categoriaNueva = Categorias(identificador,nombre, peso)
                db.session.add(categoriaNueva)
                db.session.commit()
                return((True,identificador))

        
        return( (False,0) )
#.----------------------------------------------------------------------------------------        

    def modificar(self, identificador,nombre, peso):
        """
            @brief Función que permite modificar los datos de la categoria cuyo id
                   sea "identificador".
        
            @param identificador: identificador de la categoria a modificar.
            @param nombre  : nuevo nombre para la categoria dada.
            @param peso  : peso de la categoria.
            
            @return True si se modificó la tarea dada. De lo contrario retorna
                    False.
        """
        
        # Booleanos que indican si los parámetros son del tipo correspondiente.
        idInt = type(identificador) == int
        nombreStr = type(nombre) == str
        pesoInt = type(peso) == int
        
        if ( idInt and nombreStr and pesoInt ):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            idPositivo  = identificador > 0
            nombreLongitud = 1 <= len(nombre) <= 100
            pesoPosititvo = peso >0
            
            if ( idPositivo and nombreLongitud and pesoPosititvo):
                idBuscado = db.session.query(Categorias).filter(Categorias.identificador == identificador).first()
                
                if ( idBuscado != None ):
                    db.session.query(Categorias).\
                        filter(Categorias.identificador == identificador).\
                        update({'nombre':nombre, 'peso':peso})
                    db.session.commit()
                    return( True )
                    
        return( False )

    #.-------------------------------------------------------------------------.

    def eliminar(self, identificador):
        """
            @brief Función que permite eliminar una categoria cuyo id
                   sea "identificador".
            
            @return True si se eliminó la categoria dada. De lo contrario retorna
                    False.
        """

        idInt = type(identificador) == int
        
        if (idInt):
            idPositivo = identificador >0
            
            if ( idPositivo ):
                
                categoriaBuscada = db.session.query(Categorias).\
                                filter(Categorias.identificador == identificador).\
                                first()

                if(categoriaBuscada != None):        
                    db.session.delete(categoriaBuscada)
                    db.session.commit()
                    return ( True )
            
        return ( False )
