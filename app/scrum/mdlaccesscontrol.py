# -*- coding: utf-8 -*-. 

import uuid
import hashlib
import re 
 
class clsAccessControl(object):
    
    #.------------------------------------------------------------------------------------------------.

    def __init__(self):
        
        # Expresion regular que permitirá verificar si una contraseña es válida.
        self.regularExp = ('(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d)|'
                       '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                       '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d)'
                       )

        # Expresión regular que permite verificar si una descripción dada es válida.
        self.regularExpDesc = ('-@!.,/#&+\w\s]*')

    #.------------------------------------------------------------------------------------------------.     
    
    def encript(self, value):
        """
            @brief Función que permite encriptar un string dado.

            @param value: string a encriptar.

            @return código hash que representa la encriptación de la clave dada. En caso 
                    contrario regresa el valor nulo. 
        """

        oHash=""

        # Verificación del tipo de la entrada.
        valueIsString = type(value) == str

        # Verificar la longitud del password
        if (valueIsString):
            olength_password=self.length_password(value)    
            if olength_password>=8 and olength_password<=16:
                matchObj = re.search(self.regularExp,value)
                
                print(matchObj)
                # Se verifica si la cadena introducida es valida.
                if (matchObj):        
                    # uuid es usado para generar numeros random
                    salt = uuid.uuid4().hex
                    # hash
                    oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
                    return( oHash ) 

        return( None )

    #.------------------------------------------------------------------------------------------------.
    
    def check_password(self, oPassworkEncript, oCheckPassword):
        """
            @brief Función que permite verificar si dos contraseñas son iguales.

            @param oPassworkEncript: códgido hash que representa la clave a verificar.
            @param oCheckPassword  : contraseña con la que se comparará.

            @return True si ambas claves son iguales. En caso contrario retorna False.
        """

        # Verificación del tipo de la entrada.
        checkpasswordIsString = type(oCheckPassword) == str
        if (checkpasswordIsString):
            
            # Verificar la longitud del password
            olength_password=self.length_password(oCheckPassword)
            if olength_password>=8 and olength_password<=16: 

                if ( oPassworkEncript != None ):
                    # uuid es usado para generar numeros random
                    oPassworkEncript, salt = oPassworkEncript.split(':')
                    return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
            
        return False
    
    #.------------------------------------------------------------------------------------------------.

    def length_password(self, user_password):
        """
            @brief Función que retorna la longitud de una clave.

            @param user_password: contraseña que se utilizará.

            @return entero que representa la longitud de la cadena de caracteres dada.
        """

        # uuid es usado para generar numeros random
        return len(user_password)

    #.------------------------------------------------------------------------------------------------.

    def check_descrip(self, descripc):
       """
            @brief Función que permite verificar si la descripción dada es válida.

            @param descripc: cadena de caracteres a verificar.

            @return True si la descripc es válida. De lo contrario retorna False.
       """

        # Se realiza el casteo de la descripción dada.
        descripc = str(descripc)
        lenDescrip = len(descripc)
        if (1 <= lenDescrip <= 500):        
            # Verificación de la descripción con la exp. regular.
            matchObj = re.search(self.regularExpDesc,descripc)
            
            # Se verifica si la cadena introducida es valida.
            if (matchObj):  
                return( True )
        
        return( False )   

    #.------------------------------------------------------------------------------------------------.
