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
        eliminar productos.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
from model import db, func, Productos,Historias

#.-----------------------------------------------------------------------------.

# Clase que tendra las diferentes funcionalidades de la tabla "Productos".
class clsProducto():

    #.-------------------------------------------------------------------------.
    
    def insertar(self, nombre, descripcion, escala):
        """
            @brief Funcion que permite insertar un nuevo producto en la base de 
                   datos.
            
            @param nombre : nombre del producto a insertar.
            @param descripcion : descripcion del producto a insertar.
            @param escala : escala del producto a insertar.

            @return Tupla que contiene un booleano y un numero.

                    *(True, num_productos) si se inserta correctamente el producto.
                    *(False, 0) en caso contrario.

        """

        # Booleanos que indican si los parámetros son del tipo correspondiente.
        descripcionStr = type(descripcion) == str
        nombreStr = type(nombre) == str
        escalaInt = type(escala) == int

        if ( descripcionStr and nombreStr and escalaInt ):
            # Booleano que indica si cumplen con los limites.
            descripcionLongitud = 1 <= len(descripcion) <= 500
            nombreLongitud = 1 <= len(nombre) <= 50
            escalaLongitud = 0 < escala < 3

            if ( descripcionLongitud and nombreLongitud and escalaLongitud):
                nombreBuscado = db.session.query(Productos).\
                                filter(Productos.nombre == nombre).\
                                first()

                if (nombreBuscado == None):
                    # Búsqueda del último id en la base de datos correspondiente.    
                    ultimoId = db.session.query(func.max(Productos.identificador)).\
                                    first()
                    identificador  = ultimoId[0]
                    
                    # Si no hay acciones en la base de datos, entonces se inicializa 
                    # el contador.
                    identificador = 1 if identificador == None else identificador + 1
                        
                    productoNuevo = Productos(identificador,nombre, descripcion, 
                                              escala)
                    db.session.add(productoNuevo)
                    db.session.commit()
                    return( True, identificador )
        
        return( (False, 0) )
    
    #.-------------------------------------------------------------------------.
    
    def buscarId(self, identificador):
        """
            @brief Funcion que realiza la busqueda del producto cuyo identificador
                   sea "idProducto".
            
            @param identificador: Identificador del producto a buscar.
            
            @return lista que contiene las tuplas obtenidas del subquery. De lo 
                    contrario retorna None.
        """
        
        idInt = type(identificador) == int
        
        if ( idInt ):
            idBuscado = db.session.query(Productos).\
                            filter(Productos.identificador == identificador).\
                            first()
            return( idBuscado )
        return( None )


    #.-------------------------------------------------------------------------.

    def modificar(self, identificador, nombre, descripcion, escala):

        """
            @brief Funcion que modifica los datos del producto cuyo id sea 
                   "identificador".
            
            @param identificador : id del producto a modificar.
            @param nombre : nombre del producto a insertar.
            @param descripcion : descripcion del producto a insertar.
            @param escala : escala del producto a insertar.
            
            @return True si se modifico el producto dado. De lo contrario retorna 
                    False.
        """
        
        # Booleanos que indican si los parámetros son del tipo correspondiente.
        nombreStr = type(nombre) == str
        descripcionStr = type(descripcion) == str
        idInt = type(identificador) == int
        escalaInt = type(escala) == int 
        salida = False
        
        if ( idInt and descripcionStr and nombreStr and escalaInt):
            # Booleanos que indican si se cumplen los limites.
            idPositivo     = identificador > 0
            descripcionLongitud = 1 <= len(descripcion) <= 500
            nombreLongitud = 1 <= len(nombre) <= 50
            escalaLongitud = 0 < escala < 3

            if ( idPositivo and descripcionLongitud and nombreLongitud and 
                 escalaLongitud):

                idBuscado = self.buscarId(identificador)

                if ( idBuscado != None ):
                    nombreProductoBuscado = db.session.query(Productos).\
                                            filter(Productos.nombre == nombre).\
                                            first()

                    # Se verifica si existen historias.
                    listaHistorias = db.session.query(Historias).\
                                        filter(Historias.idProducto == identificador).\
                                        first()

                    if (listaHistorias == None):
                        if ( nombreProductoBuscado == None ):                
                            db.session.query(Productos).\
                                filter(Productos.identificador == identificador).\
                                update({'nombre': nombre,
                                        'descripcion': descripcion,
                                        'escala': escala})
                            db.session.commit()
                            return( True )

                        elif (nombreProductoBuscado != None and idBuscado.nombre == nombre):
                            db.session.query(Productos).\
                                filter(Productos.identificador == identificador).\
                                update({'descripcion':(descripcion),
                                        'escala':escala})
                            db.session.commit()
                            return ( True )
                    else:
                        listaHistorias = db.session.query(Historias).\
                                        filter(Historias.idProducto == identificador).\
                                        all()
                        viejaEscala = idBuscado.escala
                        
                        if ( nombreProductoBuscado == None ):
                            db.session.query(Productos).\
                                filter(Productos.identificador == identificador).\
                                update({'nombre': nombre,
                                        'descripcion': descripcion,
                                        'escala': escala})
                                
                            db.session.commit()
                            salida = True                        

                        elif (nombreProductoBuscado != None and idBuscado.nombre == nombre):
                            db.session.query(Productos).\
                                filter(Productos.identificador == identificador).\
                                update({'descripcion':(descripcion),
                                        'escala':escala})
                            db.session.commit()
                            salida = True
                            

                    if (salida):
                        if (viejaEscala != escala):
                            if (viejaEscala == 1):
                                for hist in listaHistorias:
                                    nuevaEscala = 1 if hist.idEscala == 1 else 10 if hist.idEscala == 2 else 20
                                    db.session.query(Historias).\
                                        filter(Historias.identificador == hist.identificador).\
                                        update({'idEscala': nuevaEscala})
                        
                            else:
                                for hist in listaHistorias:
                                    nuevaEscala = 1 if hist.idEscala < 10 else 2 if 10 <= hist.idEscala < 20 else 3
                                    db.session.query(Historias).\
                                        filter(Historias.identificador == hist.identificador).\
                                        update({'idEscala': nuevaEscala})
                            db.session.commit()
                            
                        return ( salida )        
        return( salida )