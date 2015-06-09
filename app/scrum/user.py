# -*- coding: utf-8 -*-
"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121

	DESCRIPCION: Script que contiene los metodos requeridos para trabajar con la
                 tabla "User" de la base de datos dada.
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.

from model import db, Users

#-------------------------------------------------------------------------------

# Clase que tendrá las diferentes funcionalidades de la tabla "Users".
class clsUser():

    def insertar(self, nombre, username, clave, correo):
        """
            @brief Función que permite insertar un nuevo usuario en la base de 
                   datos.
            
            @param nombre: nombre completo del usuario a crear.
            @param username: username del usuario a crear.
            @param clave: contraseña del usuario a crear.
            @param correo: email del usuario a crear.

            @return True si se inserto correctamente el usuario deseado. En caso
                    contrario retorna False.
        """	
         
        # Booleanos que indican si los parámetros son del tipo correspondiente.
        nombreStr = type(nombre) == str
        usernameStr = type(username) == str
        correoStr = type(correo) == str
        claveStr  = type(clave) == str

        if ( nombreStr and usernameStr and claveStr ):
            # Booleanos que indican si los parámetros tienen el tamaño válido.
            usernameLongitud = 1 <= len(username) <= 16
            nombreLongitud   = 1 <= len(nombre) <= 50
            claveLongitud  = 1 <= len(clave)  <= 16
            correoLongitud = 1 <= len(correo) <= 30

            if (usernameLongitud and nombreLongitud and claveLongitud and 
                correoLongitud):
                
                usernameExiste = self.buscarUsername(username)
                correoExiste = self.buscarCorreo(correo)

                if (usernameExiste == None and correoExiste == None):
                    usuarioNuevo = Users(nombre, username, clave, correo)
                    db.session.add(usuarioNuevo)
                    db.session.commit()
                    return( True )
        return( False )
        
    #.-------------------------------------------------------------------------.
    
    def buscarUsername(self, username):
        """
            @brief Funcion que realiza la busqueda del usuario cuyo username sea
                   "username"
            
            @param username: username del usuario a buscar.
            
            @return tupla con la información del usuario solicitado. En caso 
                    contrario retorna None.
        """        
        
        usernameStr = type(username) == str
        if( usernameStr ):
            usuarioBuscado = db.session.query(Users).\
                                filter(Users.username == username).first()
            return( usuarioBuscado )
            
        return( None )
        
    #.-------------------------------------------------------------------------.
    
    def buscarCorreo(self, correo):
        """
            @brief Función que realiza la busqueda del usuario cuyo email sea
                   "correo"
            
            @param correo: email del usuario a buscar.
            
            @return tupla con la información del usuario solicitado. En caso 
                    contrario retorna None.
        """

        correoStr = type(correo) == str
        if( correoStr ):
            usuarioBuscado = db.session.query(Users).\
                                filter(Users.correo == correo).first()
            return(usuarioBuscado)
        return( None )

   #.--------------------------------------------------------------------------.