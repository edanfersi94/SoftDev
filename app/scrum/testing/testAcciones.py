"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcAccion.py"
    
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
from funcAccion import clsAccion



import unittest


class TestAccion(unittest.TestCase):
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsAccions.
    def testObjectExist(self):
        tempAccion = clsAccion()
        self.assertIsNotNone( tempAccion )
        model.db.session.query( model.Acciones ).delete()  # Se limpia la base de datos.
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: Buscar el id de una acci�n que exista. 
    def testfind_idAcccionExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba'
        newAccion = model.Acciones( newIdAccion, newDescripAccion ) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idAccion = 1
        query = tempAccion.find_idAccion( idAccion )
        self.assertIsNotNone( query[0] )
        model.db.session.query( model.Acciones ).delete()  # Se limpia la base de datos.
    
    # Test 3: Buscar el id de una acci�n que no exista.
    def testfind_idAccionNotExist(self):
        tempAccion = clsAccion()
        idAccion = 1000
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 4: El id de la acci�n a buscar es un string.
    def testfind_idAccionString(self):
        tempAccion = clsAccion()
        idAccion = '1'
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])
    
    # Test 5: El id de la acci�n a buscar es de tipo float.
    def testfind_idAccionFloat(self):
        tempAccion = clsAccion()
        idAccion = 1.01
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])  

    # Test 6: El id de la acci�n a buscar es nulo.
    def testfind_idAccionNone(self):
        tempAccion = clsAccion()
        idAccion = None
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])  
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Insertar una acci�n
    def testinsert_accion(self):
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        tempAccion = clsAccion()
        newDescripAccion = 'Accion 2.0'
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertTrue(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
           
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 8: Se insertara una acci�n cuyo tama�o es igual a 1.
    def testinsert_accionLen1(self):
        tempAccion = clsAccion()
        newDescripAccion = '1'
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertTrue(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.

    # Test 9: Se insertara una acci�n cuyo tama�o es igual a 500.
    def testinsert_accionLen500(self):
        tempAccion = clsAccion()
        newDescripAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertTrue(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 10: Se insertara una accion cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_accionLen0(self):
        tempAccion = clsAccion()
        newDescripAccion = ''
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.

    # Test 11: Se insertara una accion cuyo tama�o es de 501.
    def testinsert_accionLen501(self):
        tempAccion = clsAccion()
        newDescripAccion = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.

    # Test 12: Se insertara una accion cuya descripcion es un numero.
    def testinsert_accionNumber(self):
        tempAccion = clsAccion()
        newDescripAccion = 501
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.

    # Test 13: Se insertara una accion cuya descripcion dada es None.
    def testinsert_accionNone(self):
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 14: El id de la acci�n a modificar existe en la base de datos.
    def testmodify_accionExist(self):
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'AccionX'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result ) 
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.        

    # Test 15: El id de la acci�n a modificar no existe en la base de datos.
    def testmodify_accionNoExist(self):
        tempAccion = clsAccion()
        idAccion = 20
        newDescripAccion = 'Esto sigue siendo una prueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result ) 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 16: El id de la acci�n a modificar existe en la base de datos y su
    #          valor es igual a 1. 
    def testmodify_accionIdExistIqual1(self):
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        

        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'esto sigue siendo una prueva V2'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result ) 
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos. 

    
    # Test 17: El id de la acci�n a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_accionIdExistNewDescripLen1(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'l'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue(result)
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.   
    
    # Test 18: El id de la acci�n a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_accionIdExistNewDescripLen500(self):
        
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'y'*500
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        
    
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 19: El id de la acci�n a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_accionIdExistIqual1NewDescripLen1(self):
        newIdAccion = 1
        newDescripAccion = 'z'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'z'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos. 
    
    # Test 20: El id de la acci�n a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_accionIdExistIqual1NewDescripLen500(self):
        
        newIdAccion = 1
        newDescripAccion = 'x'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result ) 
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.

    ### CASOS INVALIDOS( Casos Malicia )
    # Test 21: El id dado de la acci�n a modificar es un string.
    def testmodify_accionIdString(self):        
        tempAccion = clsAccion()
        idAccion = '1'
        newDescripAccion = 'Axx'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )    
        
    # Test 22: El id dado de la acci�n a modificar es un numero negativo.    
    def testmodify_accionIdNegative(self):        
        tempAccion = clsAccion()
        idAccion = -1
        newDescripAccion = 'accion de prueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   

    # Test 23: El id dado de la acci�n a modificar es un float.
    def testmodify_accionIdFloat(self):        
        tempAccion = clsAccion()
        idAccion = 1.0
        newDescripAccion = 'accion de prueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   
        
    # Test 24: El id dado de la acci�n a modificar es None.         
    def testmodify_accionIdNone(self):        
        tempAccion = clsAccion()
        idAccion = None
        newDescripAccion = 'accionPrueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   
    
    # Test 25: La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_accionDescripIsEmpty(self):   
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
             
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = ''
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.    
        
    # Test 26: La nueva descripci�n para la acci�n a modificar es de longitud 501.    
    def testmodify_accionDescripLen501(self):     
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
           
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'r'*501
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.    

    # Test 27: La nueva descripci�n para la acci�n a modificar es un numero.
    def testmodify_accionDescripIsNumber(self):        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 12345
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.    
        
    # Test 28: La nueva descripci�n para la acci�n a modificar es None. 
    def testmodify_accionDescripNone(self):   
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = None
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.    

    #.-------------------------------------------------------------------.  