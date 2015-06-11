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


class TestActores(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Actores ).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Pila ).delete() 
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsActor.
    def testObjectExist(self):
        tempActor = clsActor()
        self.assertIsNotNone( tempActor )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Buscar el id de un actor que exista en la base de datos de un elemento. 
    def testfind_IdActorExist(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        newIdActor = 1
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()

    # Buscar el id de un actor con base de datos vacia
    def testfind_IdActorNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newIdActor = 1000
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un actor con base de datos un elemento y busqueda no exitosa
        
    def testfind_IdActorNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
        
        
        tempActor = clsActor()
        newIdActor = 2
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un actor con base de datos de varios elemento y busqueda no exitosa   
    def testfind_IdActorNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdActor = indice
            newDescripActor  = 'Esto es una prueba ' + str(indice)
            newNameActor='Joel'
            newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
            model.db.session.add(newActor)
            model.db.session.commit()   
        
        
        tempActor = clsActor()
        newIdActor = 5
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un actor con base de datos de varios elemento y busqueda exitosa   
    def testfind_IdActorExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdActor = indice
            newDescripActor  = 'Esto es una prueba ' + str(indice)
            newNameActor='Joel'
            newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
            model.db.session.add(newActor)
            model.db.session.commit()   
        
        tempActor = clsActor()
        newIdActor = 3
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del actor a buscar es un string.
    def testfind_IdActorString(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto= model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newIdActor = '1'
        query = tempActor.find_idActor(newIdProducto, newIdActor )
        self.assertEqual(query,[])
        
        self.vaciarBaseDeDatos()
        
    # El id del actor a buscar es de tipo float.
    def testfind_IdActorFloat(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto= model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newIdActor = 1.01
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del actor a buscar es nulo.
    def testfind_IdActorNone(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto= model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newIdActor = None
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del actor a buscar es negativo.
    def testfind_IdActorNegative(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto= model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newIdActor = -3
        query = tempActor.find_idActor( newIdProducto,newIdActor )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un actor con un elemento en la base de datos
    def testinsert_ActorBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto =' Descripcion Producto.. '
        newProducto  = model.Pila(newIdProducto,newDescripProducto )
        model.db.session.add(newProducto )
        model.db.session.commit() 
        
        newIdActor = 2
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   

        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'actor 2.0'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un actor con la base de datos vacia.
    def testinsert_ActorBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        

        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'actor 2.0'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un actor con varios elementos en la base de datos.
    def testinsert_ActorBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(5,10,1):
            newIdActor = indice
            newDescripActor  = 'Esto es una prueba ' + str(indice)
            newNameActor='Joel'
            newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
            model.db.session.add(newActor)
            model.db.session.commit()   
            
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'actor 2.0'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un actor cuyo tama�o es igual a 1.
    def testinsert_ActorDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = '1'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertTrue(result)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un actor cuyo tama�o es igual a 500.
    def testinsert_ActorDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertTrue(result)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un actor cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_ActorDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = ''
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuyo tama�o es de 501.
    def testinsert_ActorDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor   )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una actor cuya descripcion es un numero.
    def testinsert_ActorDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        
        newNameActor='Joel mejorado'
        newDescripActor = 501
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuya descripcion dada es None.
    def testinsert_ActorDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = None
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuya descripcion dada es Float.
    def testinsert_ActorDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 0.54
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #Se insertara un actor con id string
    def testinsert_ActorIdString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'ola k ase'
        result = tempActor.insert_Actor( 'problem?',newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un actor con id Float
    def testinsert_ActorIdFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()

        newNameActor='Joel mejorado'
        newDescripActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insert_Actor( 1.32,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                

    # Se insertara un actor con id float.
    def testinsert_ActorIdNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'None.. uff caiste'
        result = tempActor.insert_Actor( None,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id maximo.
    def testinsert_ActorIdGrant(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'None.. uff caiste'
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo.
    def testinsert_ActorIdNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'None.. uff caiste'
        result = tempActor.insert_Actor(-3,newNameActor, newDescripActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion entero.
    def testinsert_ActorIdStringDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 123
        result = tempActor.insert_Actor( 'newIdProducto',newNameActor, newDescripActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion float.
    def testinsert_ActorIdStringDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 23.23
        result = tempActor.insert_Actor( 'newIdProducto',newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion None.
    def testinsert_ActorIdStringDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = None
        result = tempActor.insert_Actor( 'newIdProducto',newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion tamaño 500.
    def testinsert_ActorIdStringDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*500
        result = tempActor.insert_Actor( 'newIdProducto',newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id string y descripcion tamaño 501.
    def testinsert_ActorIdStringDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*501
        result = tempActor.insert_Actor( 'newIdProducto',newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion entero.
    def testinsert_ActorIdFloatDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 32
        result = tempActor.insert_Actor( 43.32,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion float.
    def testinsert_ActorIdFloatDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 32.323
        result = tempActor.insert_Actor( 43.32,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion None.
    def testinsert_ActorIdFloatDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = None
        result = tempActor.insert_Actor( 43.32,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion tamaño 500.
    def testinsert_ActorIdFloatDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*500
        result = tempActor.insert_Actor( 43.32,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion tamaño 501.
    def testinsert_ActorIdFloatDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()

        newNameActor='Joel mejorado'
        newDescripActor = 'y'*501
        result = tempActor.insert_Actor( 43.32,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion entero.
    def testinsert_ActorIdNoneDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 34
        result = tempActor.insert_Actor( None,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion float.
    def testinsert_ActorIdNoneDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 34.23
        result = tempActor.insert_Actor( None,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion None.
    def testinsert_ActorIdNoneDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = None
        result = tempActor.insert_Actor( None,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id None y descripcion 500.
    def testinsert_ActorIdNoneDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*500
        result = tempActor.insert_Actor( None,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion 501.
    def testinsert_ActorIdNoneDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*501
        result = tempActor.insert_Actor( None,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion entero.
    def testinsert_ActorIdGrantDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 34
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id Grande y descripcion float.
    def testinsert_ActorIdGrantDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 34.32
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion None.
    def testinsert_ActorIdGrantDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = None
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion 500.
    def testinsert_ActorIdGrantDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*500
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion 501.
    def testinsert_ActorIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*501
        result = tempActor.insert_Actor( newIdProducto,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
 
     # Se insertara un actor con id Negativo y descripcion entero.
    def testinsert_ActorIdNegativeDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 34
        result = tempActor.insert_Actor( -3,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id negativo y descripcion float.
    def testinsert_ActorIdNegativeDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 34.32
        result = tempActor.insert_Actor( -3,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo y descripcion None.
    def testinsert_ActorIdNegativeDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = None
        result = tempActor.insert_Actor( -3,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo y descripcion 500.
    def testinsert_ActorIdNegativeDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*500
        result = tempActor.insert_Actor(-3,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo y descripcion 501.
    def testinsert_ActorIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        newNameActor='Joel mejorado'
        newDescripActor = 'y'*501
        result = tempActor.insert_Actor( -3 ,newNameActor, newDescripActor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del actor a modificar existe en la base de datos de un elemento.
    def testmodify_ActorExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   

        
        tempActor = clsActor()
        newIdActor = 1
        newNameActor='otro joel, no es el mismo :p '
        newDescripActor = 'actorX'
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testmodify_ActorNotExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
      
        tempActor=clsActor()  
        newIdActor = 1
        newNameActor='otro joel, no es el mismo :p '
        newDescripActor = 'actorX'
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del actor a modificar existe en la base de datos de varios actors 
    def testmodify_ActorIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(1,10,1):
            newIdActor = indice
            newDescripActor  = 'Esto es una prueba' + str(indice)
            newNameActor='Joel'+ str(indice)
            newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
            model.db.session.add(newActor)
            model.db.session.commit()    
            
        tempActor=clsActor()
        newIdActor = 2
        newNameActor='otro joel, no es el mismo :p '
        newDescripActor = 'actorX'
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del actor a modificar no existe en la base de datos de varios actors 
    def testmodify_ActorIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(1,10,1):
            newIdActor = indice
            newDescripActor  = 'Esto es una prueba' + str(indice)
            newNameActor='Joel'+ str(indice)
            newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
            model.db.session.add(newActor)
            model.db.session.commit()   
            
        tempActor = clsActor()
        newIdActor= 43
        newNameActor='otro joel, no es el mismo :p '
        newDescripActor = 'actorX'
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del actor a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_ActorIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = 'l'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del actor a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_ActorIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = 'y'*500
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del actor a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_ActorIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = 'z'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del actor a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_ActorIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del actor a modificar es un string.
    def testmodify_ActorIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
            
        tempActor = clsActor()
        newIdActor = '1'
        newDescripActor = 'Axx'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testmodify_ActorIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
           
        tempActor = clsActor()
        newIdActor = -1
        newDescripActor = 'actor de prueba'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del actor a modificar es un float.
    def testmodify_ActorIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
          
        tempActor = clsActor()
        newIdActor = 1.0
        newDescripActor = 'actor de prueba'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del actor a modificar es None.         
    def testmodify_ActorIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
             
        tempActor = clsActor()
        newIdActor = None
        newDescripActor = 'actorPrueba'
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_ActorDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
             
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = ''
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es de longitud 501.    
    def testmodify_ActorDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = 'r'*501
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el actor a modificar es un numero.
    def testmodify_ActorDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
        
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = 12345
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el actor a modificar es None. 
    def testmodify_ActorDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()    
          
        tempActor = clsActor()
        newIdActor = 1
        newDescripActor = None
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es Entero y id string . 
    def testmodify_ActorIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()    
          
        tempActor = clsActor()
        newIdActor = 'malo'
        newDescripActor = 1212
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es Float y id string . 
    def testmodify_ActorIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()    
          
        tempActor = clsActor()
        newIdActor = 'malo'
        newDescripActor = 1212.23
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id string . 
    def testmodify_ActorIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()    
          
        tempActor = clsActor()
        newIdActor = 'malo'
        newDescripActor = None
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 500 y id string . 
    def testmodify_ActorIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()     
          
        tempActor = clsActor()
        newIdActor = 'malo'
        newDescripActor = 'y'*500
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id string . 
    def testmodify_ActorIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        newIdActor = 'malo'
        newDescripActor = 'y'*501
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño Entero y id float . 
    def testmodify_ActorIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        newIdActor = 23.23
        newDescripActor = 23
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño Float y id float . 
    def testmodify_ActorIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        newIdActor = 23.23
        newDescripActor = 23.23
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id float . 
    def testmodify_ActorIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()
          
        tempActor = clsActor()
        newIdActor = 23.23
        newDescripActor = None
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el actor a modificar es tamaño 500 y id float . 
    def testmodify_ActorIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        newIdActor = 23.23
        newDescripActor = 'y'*500
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id float . 
    def testmodify_ActorIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()
          
        tempActor = clsActor()
        newIdActor = 23.23
        newDescripActor = 'y'*501
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es entero y id None . 
    def testmodify_ActorIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = None
        newDescripActor = 23
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es float y id None . 
    def testmodify_ActorIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = None
        newDescripActor = 23.23
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id None . 
    def testmodify_ActorIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = None
        newDescripActor = None
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 500 y id None . 
    def testmodify_ActorIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
          
        tempActor = clsActor()
        newIdActor = None
        newDescripActor = 'y'*500
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id None . 
    def testmodify_ActorIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = None
        newDescripActor = 'y'*501
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el actor a modificar es Entero y id MAX . 
    def testmodify_ActorIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = 2**31 -1
        newDescripActor = 43
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es float y id MAX . 
    def testmodify_ActorIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor = 2**31 -1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = 2**31 -1
        newDescripActor = 43.323
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id MAX . 
    def testmodify_ActorIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor =  2**31 -1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = 2**31 -1
        newDescripActor = None
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 500 y id MAX . 
    def testmodify_ActorIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor =  2**31 -1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit() 
          
        tempActor = clsActor()
        newIdActor = 2**31 -1
        newDescripActor = 'y'*500
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id MAX . 
    def testmodify_ActorIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdActor =  2**31 -1
        newDescripActor  = 'Esto es una prueba'
        newNameActor='Joel'
        newActor = model.Actores( newIdProducto,newIdActor ,newNameActor, newDescripActor  ) 
        model.db.session.add(newActor)
        model.db.session.commit()  
          
        tempActor = clsActor()
        newIdActor = 2**31 -1
        newDescripActor = 'y'*501
        newNameActor='otro joel, no es el mismo :p '
        result = tempActor.modify_Actor(  newIdProducto,newIdActor ,newNameActor, newDescripActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.