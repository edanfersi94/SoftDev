"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcObjetivo.py"
    
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

# PATH que permite utilizar al modulo "dpt.py"
sys.path.append('../')
from funcObjetivo import clsObjetivo



import unittest


class TestObjetivo(unittest.TestCase):
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsObjetivo.
    def testObjectExist(self):
        tempObj = clsObjetivo()
        self.assertIsNotNone( tempObj )
        model.db.session.query( model.Objetivo ).delete()  # Se limpia la base de datos.
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: Buscar el id de un objetivo que exista. 
    def testfind_idObjetivoExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo ) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        query = tempObjetivo.find_idObjetivo( idObjetivo )
        self.assertIsNotNone( query[0] )
        model.db.session.query( model.Objetivo ).delete()  # Se limpia la base de datos.
    
    # Test 3: Buscar el id de un objetivo que no exista.
    def testfind_idObjetivoNotExist(self):
        tempObjetivo = clsObjetivo()
        idObjetivo = 1000
        query = tempObjetivo.find_idObjetivo( idObjetivo )
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 4: El id del objetivo a buscar es un string.
    def testfind_idObjetivoString(self):
        tempObjetivo = clsObjetivo()
        idObjetivo = '1'
        query = tempObjetivo.find_idObjetivo( idObjetivo )
        self.assertEqual(query,[])
    
    # Test 5: El id del objetivo a buscar es de tipo float.
    def testfind_idObjetivoFloat(self):
        tempObjetivo = clsObjetivo()
        idObjetivo = 1.01
        query = tempObjetivo.find_idObjetivo( idObjetivo )
        self.assertEqual(query,[])  

    # Test 6: El id del objetivo a buscar es nulo.
    def testfind_idObjetivoNone(self):
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        query = tempObjetivo.find_idObjetivo( idObjetivo )
        self.assertEqual(query,[])  
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Insertar un objetivo
    def testinsert_Objetivo(self):

        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertTrue(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.
           
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 8: Se insertara un objetivo cuyo tama�o es igual a 1.
    def testinsert_ObjetivoLen1(self):
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = '1'
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertTrue(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.

    # Test 9: Se insertara un objetivo cuyo tama�o es igual a 500.
    def testinsert_ObjetivoLen500(self):
        tempObjetivo = clsObjetivo()
        newDescripObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertTrue(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 10: Se insertara un Objetivo cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_ObjetivoLen0(self):
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = ''
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertFalse(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.

    # Test 11: Se insertara un Objetivo cuyo tama�o es de 501.
    def testinsert_ObjetivoLen501(self):
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertFalse(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.

    # Test 12: Se insertara una Objetivo cuya descripcion es un numero.
    def testinsert_ObjetivoNumber(self):
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 501
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertFalse(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.

    # Test 13: Se insertara un Objetivo cuya descripcion dada es None.
    def testinsert_ObjetivoNone(self):
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( newDescripObjetivo )
        self.assertFalse(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 14: El id del objetivo a modificar existe en la base de datos.
    def testmodify_ObjetivoExist(self):
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoX'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertTrue( result ) 
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.        

    # Test 15: El id del ojetivo a modificar no existe en la base de datos.
    def testmodify_ObjetivoNoExist(self):
        tempObjetivo = clsObjetivo()
        idObjetivo = 20
        newDescripObjetivo = 'Esto sigue siendo una prueba'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result ) 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 16: El id del objetivo a modificar existe en la base de datos y su
    #          valor es igual a 1. 
    def testmodify_ObjetivoIdExistIqual1(self):
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        

        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'esto sigue siendo una prueva V2'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertTrue( result ) 
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos. 

    
    # Test 17: El id del objetivo a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_ObjetivoIdExistNewDescripLen1(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'l'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertTrue(result)
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.   
    
    # Test 18: El id del objetivo a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_ObjetivoIdExistNewDescripLen500(self):
        
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        
    
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 19: El id del objetivo a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_ObjetivoIdExistIqual1NewDescripLen1(self):
        newIdObjetivo = 1
        newDescripObjetivo = 'z'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'z'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertTrue( result )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos. 
    
    # Test 20: El id del objetivo a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_ObjetivoIdExistIqual1NewDescripLen500(self):
        
        newIdObjetivo = 1
        newDescripObjetivo = 'x'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertTrue( result ) 
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.

    ### CASOS INVALIDOS( Casos Malicia )
    # Test 21: El id dado del objetivo a modificar es un string.
    def testmodify_ObjetivoIdString(self):        
        tempObjetivo = clsObjetivo()
        idObjetivo = '1'
        newDescripObjetivo = 'Axx'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )    
        
    # Test 22: El id dado del obetivo a modificar es un numero negativo.    
    def testmodify_ObjetivoIdNegative(self):        
        tempObjetivo = clsObjetivo()
        idObjetivo = -1
        newDescripObjetivo = 'Objetivo de prueba'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )   

    # Test 23: El id dado del objetivo a modificar es un float.
    def testmodify_ObjetivoIdFloat(self):        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1.0
        newDescripObjetivo = 'Objetivo de prueba'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )   
        
    # Test 24: El id dado del objetivo a modificar es None.         
    def testmodify_ObjetivoIdNone(self):        
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )   
    
    # Test 25: La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_ObjetivoDescripIsEmpty(self):   
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = ''
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.    
        
    # Test 26: La nueva descripci�n para el objetivo a modificar es de longitud 501.    
    def testmodify_ObjetivoDescripLen501(self):     
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()
           
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'r'*501
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.    

    # Test 27: La nueva descripci�n para el objetivo a modificar es un numero.
    def testmodify_ObjetivoDescripIsNumber(self):        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 12345
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.    
        
    # Test 28: La nueva descripci�n para el objetivo a modificar es None. 
    def testmodify_ObjetivoDescripNone(self):   
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdObjetivo, newDescripObjetivo) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = None
        result = tempObjetivo.modify_Objetivo( idObjetivo, newDescripObjetivo )
        self.assertFalse( result )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.    

    #.-------------------------------------------------------------------.  