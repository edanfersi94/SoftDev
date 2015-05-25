"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcActor.py"
    
"""

#--------------------------------------------------------------------------------------

# Librerias a utilizar

import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

# PATH que permite utilizar al modulo "funcActor.py"
sys.path.append('../')
from funcActor import clsActor

import unittest

class TestActor(unittest.TestCase):

    #.------------------------------------------------------.
    # VERIFICACION DE LA CLASE

    # Se crea el objeto de la clase clsActor
    def TestObjectExist(self):
        tempActor = clsActor()
        self.assertIsNone( tempActor )
        model.db.session.query( model.Actores ).delete() # Se limpia la base de datos


    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Buscar el id de un Actor que exista. 
    def testfind_idActorExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        
        newIdActor = 1
        newName='Joel'
        newDescripActor = 'Esto es una prueba'
        newActor = model.Actores(newIdActor,newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        idActor = 1
        query = tempActor.find_idActor(idActor)
        self.assertIsNotNone(query[0])
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
    
    # Buscar el id de un Actor que no exista.
    def testfind_idActorNotExist(self):
        
        tempActor = clsActor()
        idActor = 1000
        query = tempActor.find_idActor( idActor )
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # El id del Actor a buscar es un string.
    def testfind_idActorString(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        idActor = '1'
        query = tempActor.find_idActor( idActor )
        self.assertEqual(query,[])
    
    # El id del Actor a buscar es de tipo float.
    def testfind_idActorFloat(self):
        tempActor = clsActor()
        idActor = 1.01
        query = tempActor.find_idActor( idActor )
        self.assertEqual(query,[])  

    # El id del Actor a buscar es nulo.
    def testfind_idActorNone(self):
        tempActor = clsActor()
        idActor = None
        query = tempActor.find_idActor( idActor )
        self.assertEqual(query,[])  

#.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un actor
    def testinsert_Actor(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  

        tempActor = clsActor()
        newName= 'joel'
        newDescripActor = 'Actor 2.0'
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
           
    ### CASOS VALIDOS( Casos Fronteras )
    # Se insertara un actor cuyo tama�o descripcion es igual a 1.
    def testinsert_ActorDescripLen1(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor = '1'
        result = tempActor.insert_Actor( newName,newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara un actor cuyo tama�o descripcion es igual a 500.
    def testinsert_ActorDescripLen500(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insert_Actor(newName,newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Se insertara un Actor cuyo tama�o descripcion es 0 (Cadena Vac�a).
    def testinsert_ActorDescripLen0(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor = ''
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara un Actor cuyo tama�o descripchion es de 501.
    def testinsert_ActorDescripLen501(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara una Actor cuya descripcion es un numero.
    def testinsert_ActorDescripNumber(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor = 501
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara un Actor cuya descripcion dada es None.
    def testinsert_ActorDescripNone(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor = None
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara un Actor cuya name dada es 1.
    def testinsert_ActorNameLen1(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= '1'
        newDescripActor = '1asdas'
        result = tempActor.insert_Actor( newName,newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara un actor cuyo tama�o descripcion es igual a 500.
    def testinsert_ActorDescripLen500(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'joel'
        newDescripActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insert_Actor(newName,newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Se insertara un Actor cuyo name es 0 (Cadena Vac�a).
    def testinsert_ActorNameLen0(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= ''
        newDescripActor = 'ola k ase?'
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    # Se insertara un Actor cuyo tama�o es de name 501.
    def testinsert_ActorNameLen501(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        newDescripActor = 'ola k ase?'
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    #  Se insertara una Actor cuya name es un numero.
    def testinsert_ActorNameNumber(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 501
        newDescripActor = 'ola k ase?'
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    #  Se insertara un Actor cuya name dada es None.
    def testinsert_ActorNameNone(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= None
        newDescripActor = 'ola k ase?'
        result = tempActor.insert_Actor(newName, newDescripActor )
        self.assertFalse(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
        
    # Se insertara un actor cuyo tama�o name es igual a 50.
    def testinsert_ActorNameLen50(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        newName= 'j'*50
        newDescripActor = 'ola k ase? viendo mis casos de prueba o k ase?'
        result = tempActor.insert_Actor(newName,newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.        
        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del actor a modificar existe en la base de datos.
    def testmodify_ActorExist(self):
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newName= 'joel23'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor,newName, newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit() 
        
        tempActor = clsActor()
        idActor = 1
        newName="Nicolas"
        newDescripActor = 'ActorX'
        result = tempActor.modify_Actor( idActor, newName,newDescripActor )
        self.assertTrue( result ) 
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.        

    # El id del actor a modificar no existe en la base de datos.
    def testmodify_ActorNoExist(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        idActor = 20
        
        newName= 'joel'
        newDescripActor = 'Esto sigue siendo una prueba'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result ) 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del actor a modificar existe en la base de datos y su
    #          valor es igual a 1. 
    def testmodify_ActorIdExistIqual1(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        newIdActor = 1
        
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor, newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit() 
        

        tempActor = clsActor()
        idActor = 1
        newName='noc'
        newDescripActor = 'esto sigue siendo una prueva V2'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertTrue( result ) 
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos. 

    
    # El id del actor a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_ActorIdExistNewDescripLen1(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor,newName, newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit() 
        
        tempActor = clsActor()
        idActor = 1
        newName='Nicol'
        newDescripActor = 'l'
        result = tempActor.modify_Actor( idActor, newName,newDescripActor )
        self.assertTrue(result)
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.   
    
    # El id del actor a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_ActorIdExistNewDescripLen500(self):
        
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor, newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit() 
        
        tempActor = clsActor()
        idActor = 1
        newName='Nicolas'
        newDescripActor = 'y'*500
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        
        self.assertTrue( result )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
        
    
    ### CASOS VALIDOS( Casos Esquinas )
    # El id del actor a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_ActorIdExistIqual1NewDescripLen1(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'z'
        newActor = model.Actores( newIdActor, newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idActor = 1
        newName='Nicolas'
        newDescripActor = 'z'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertTrue( result )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos. 
    
    # El id del actor a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_ActorIdExistIqual1NewDescripLen500(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'x'
        newActor = model.Actores( newIdActor,newName, newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idActor = 1
        newName='Nicoals'
        newDescripActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertTrue( result ) 
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.

    ### CASOS INVALIDOS( Casos Malicia )
    #El id dado del actor a modificar es un string.
    def testmodify_ActorIdString(self):       
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.   
        tempActor = clsActor()
        idActor = '1'
        
        newName= 'joel'
        newDescripActor = 'Axx'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )    
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testmodify_ActorIdNegative(self):  
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.        
        tempActor = clsActor()
        idActor = -1
        
        newName= 'joel'
        newDescripActor = 'Actor de prueba'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )   

    # El id dado del actor a modificar es un float.
    def testmodify_ActorIdFloat(self):    
              
        tempActor = clsActor()
        idActor = 1.0
        
        newName= 'joel'
        newDescripActor = 'Actor de prueba'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )   
        
    # El id dado del actor a modificar es None.         
    def testmodify_ActorIdNone(self):    
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.      
        tempActor = clsActor()
        idActor = None
        
        newName= 'joel'
        newDescripActor = 'ActorPrueba'
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )   
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_ActorDescripIsEmpty(self):   
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor, newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()
             
        tempActor = clsActor()
        idActor = 1
        newDescripActor = ''
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.    
        
    # La nueva descripci�n para el actor a modificar es de longitud 501.    
    def testmodify_ActorDescripLen501(self):     
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor,newName, newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()
           
        tempActor = clsActor()
        idActor = 1
        newDescripActor = 'r'*501
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.    

    # La nueva descripci�n para el actor a modificar es un numero.
    def testmodify_ActorDescripIsNumber(self): 
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.       
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor, newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idActor = 1
        newDescripActor = 12345
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.    
        
    # La nueva descripci�n para el actor a modificar es None. 
    def testmodify_ActorDescripNone(self):   
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        
        newIdActor = 1
        newName= 'joel'
        newDescripActor = 'Esto es una prueba.'
        newActor = model.Actores( newIdActor,newName, newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idActor = 1
        newDescripActor = None
        result = tempActor.modify_Actor( idActor,newName, newDescripActor )
        self.assertFalse( result )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.    

    #.-------------------------------------------------------------------. 

    # FUNCION BUSCAR NOMBRE ACTOR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El nombre del actor a buscar existe en la base de datos.
    def testfind_nameActor(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura que es valida      
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        
        newIdActor = 1
        newName='Joel'
        newDescripActor = 'Esto es una prueba'
        newActor = model.Actores(newIdActor,newName,newDescripActor) 
        model.db.session.add(newActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        idActor = 1
        query = tempActor.find_nameActor(newName)
        self.assertIsNotNone(query[0])
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
    
    # Buscar el name de un Actor que no exista.
    def testfind_nameActorNotExist(self):
        
        tempActor = clsActor()
        nameActor = 'carlitos'
        query = tempActor.find_nameActor(nameActor)
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # El name del Actor a buscar es un entero.
    def testfind_nameActorInt(self):
        
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.  
        tempActor = clsActor()
        nameActor = 123
        query = tempActor.find_nameActor( nameActor )
        self.assertEqual(query,[])
    
    # El name del Actor a buscar es de tipo float.
    def testfind_nameActorFloat(self):
        tempActor = clsActor()
        nameActor = 1.01
        query = tempActor.find_nameActor(nameActor)
        self.assertEqual(query,[])  

    # El name del Actor a buscar es nulo.
    def testfind_nameActorNone(self):
        tempActor = clsActor()
        nameActor = None
        query = tempActor.find_nameActor(nameActor)
        self.assertEqual(query,[])  

 