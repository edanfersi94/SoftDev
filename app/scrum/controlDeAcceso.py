# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        Módulo que contiene los métodos que permitirán verificar si las claves y 
        las descripciones son válidas.
"""

#.-----------------------------------------------------------------------------.

# Funciones a importar:
import re 
import uuid
import hashlib
 
#.-----------------------------------------------------------------------------.

# Clases que tendrá los diferentes métodos que permitiran verificar claves y 
# descripciones.
class clsControlDeAcceso(object):
    
    #.-------------------------------------------------------------------------.

    def __init__(self):
        
        # Expresion regular que permitirá verificar si una contraseña es válida.
        self.expRegular = ('(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d)|'
                       '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d)'
                       )

    #.-------------------------------------------------------------------------.     
    
    def encriptar(self, clave):
        """
            @brief Función que permite encriptar contraseñas dadas.

            @param clave: string a encriptar.

            @return código hash que representa la encriptación de la clave dada. 
                    En caso contrario regresa el valor nulo. 
        """

        # Booleano que indica si el parámetro es del tipo correspondiente.
        claveStr = type(clave) == str

        if (claveStr):
            # Booleano que indica si el parámetro tiene el tamaño válido.
            claveLongitud = self.longitudPassword(clave)    
            if ( 8 <= claveLongitud <= 16 ):
                objGenerado = re.search(self.expRegular, clave)
                
                # Se verifica si la cadena introducida es valida.
                if (objGenerado):        
                    
                    # uuid es usado para generar numeros random
                    salt = uuid.uuid4().hex
                    codigoHash= (hashlib.sha256(salt.encode() 
                                               + clave.encode()).hexdigest()
                                               + ':' + salt)
                    return( codigoHash ) 

        return( None )

    #.-------------------------------------------------------------------------.
    
    def verificarPassword(self, claveEncriptada, claveVerificar):
        """
            @brief Función que permite verificar si dos contraseñas son iguales.

            @param claveEncriptada: códgido hash que representa la clave a 
                                    verificar.
            @param claveVerificar : contraseña con la que se comparará.

            @return True si ambas claves son iguales. En caso contrario retorna 
                    False.
        """

        # Booleanos que indican si los parámetros son del tipo correspondiente.
        claveEncriptadaNoNone = claveEncriptada != None
        claveVerificarStr = type(claveVerificar) == str
        
        if (claveEncriptadaNoNone and claveVerificarStr):
            
            # Booleano que indica si el parámetro tiene el tamaño válido.
            claveVerificarLongitud = self.longitudPassword(claveVerificar)
            if ( 8 <= claveVerificarLongitud <= 16 ): 
                # uuid es usado para generar numeros random
                claveEncriptada, salt = claveEncriptada.split(':')
                return claveEncriptada == (hashlib.sha256(salt.encode() + 
                                            claveVerificar.encode()).hexdigest())
            
        return( False )
    
    #.-------------------------------------------------------------------------.

    def longitudPassword(self, clave):
        """
            @brief Función que retorna la longitud de una clave dada.

            @param clave: contraseña que se utilizará.

            @return entero que representa la longitud de la cadena de caracteres
                    dada.
        """
        return( len(clave) )

    #.-------------------------------------------------------------------------.

    def verificarDescripcion(self, descripcion):
        """
            @brief Función que verifica si una descripción dada es válida.

            @param descripcion: cadena de caracteres a verificar.

            @return True si la cadena es válida. En caso contrario retorna False.
        """

        clean = re.compile(r'<.*?>')
        resultClean = clean.sub('', descripcion)
    
        if (len(resultClean) > 0):
            return( True )
        return( False )

    #.-------------------------------------------------------------------------.
