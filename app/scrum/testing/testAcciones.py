"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcaccion.py"
    
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

sys.path.append('../')
from funcAccion import clsAccion



import unittest


class TestAccion(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Acciones ).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Pila ).delete() 
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsAccion.
    def testObjectExist(self):
        tempAccion = clsAccion()
        self.assertIsNotNone( tempAccion )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Buscar el id de un accion que exista en la base de datos de un elemento. 
    def testfind_idAccionExist(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 1
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()

    # Buscar el id de un accion con base de datos vacia
    def testfind_idAccionNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1000
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un accion con base de datos un elemento y busqueda no exitosa
        
    def testfind_idAccionNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdAccion = 2
        newDescripAccion = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 1
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un accion con base de datos de varios elemento y busqueda no exitosa   
    def testfind_idAccionNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdAccion = indice
            newDescripAccion = 'Descripcion ' + str(indice)
            newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
            model.db.session.add(newAccion)
            model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 5
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un accion con base de datos de varios elemento y busqueda exitosa   
    def testfind_idAccionExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdAccion = indice
            newDescripAccion = 'Descripcion ' + str(indice)
            newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
            model.db.session.add(newAccion)
            model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 3
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del accion a buscar es un string.
    def testfind_idAccionString(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = '1'
        query = tempAccion.find_idAccion(newIdProducto, idaccion )
        self.assertEqual(query,[])
        
        self.vaciarBaseDeDatos()
        
    # El id del accion a buscar es de tipo float.
    def testfind_idAccionFloat(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1.01
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del accion a buscar es nulo.
    def testfind_idAccionNone(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = None
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del accion a buscar es negativo.
    def testfind_idAccionNegative(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = -3
        query = tempAccion.find_idAccion( newIdProducto,idaccion )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un accion con un elemento en la base de datos vacia.
    def testinsert_AccionBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdAccion = 3
        newDescripAccion = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
        

        tempAccion = clsAccion()
        newDescripAccion = 'accion 2.0'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un accion con la base de datos vacia.
    def testinsert_AccionBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        

        tempAccion = clsAccion()
        newDescripAccion = 'accion 2.0'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un accion con varios elementos en la base de datos.
    def testinsert_AccionBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(5,10,1):
            newIdAccion = indice
            newDescripAccion = 'Descripcion ' + str(indice)
            newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
            model.db.session.add(newAccion)
            model.db.session.commit()   
            
        tempAccion = clsAccion()
        newDescripAccion = 'accion 2.0'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un accion cuyo tama�o es igual a 1.
    def testinsert_AccionDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = '1'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un accion cuyo tama�o es igual a 500.
    def testinsert_AccionDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un accion cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_AccionDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = ''
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion cuyo tama�o es de 501.
    def testinsert_AccionDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una accion cuya descripcion es un numero.
    def testinsert_AccionDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 501
        result = tempAccion.insert_Accion(newIdProducto, newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion cuya descripcion dada es None.
    def testinsert_AccionDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion cuya descripcion dada es Float.
    def testinsert_AccionDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 0.54
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #Se insertara un accion con id string
    def testinsert_AccionIdString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'ola k ase'
        result = tempAccion.insert_Accion( 'error',newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un accion con id Float
    def testinsert_AccionIdFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.insert_Accion(1.32,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                

    # Se insertara un accion con id float.
    def testinsert_AccionIdNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'None.. uff caiste'
        result = tempAccion.insert_Accion( None,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id maximo.
    def testinsert_AccionIdGrant(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'None.. uff caiste'
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo.
    def testinsert_AccionIdNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'None.. uff caiste'
        result = tempAccion.insert_Accion(-3,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion entero.
    def testinsert_AccionIdStringDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 123
        result = tempAccion.insert_Accion( 'newIdProducto',newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion float.
    def testinsert_AccionIdStringDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 23.23
        result = tempAccion.insert_Accion( 'newIdProducto',newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion None.
    def testinsert_AccionIdStringDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( 'newIdProducto',newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion tamaño 500.
    def testinsert_AccionIdStringDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*500
        result = tempAccion.insert_Accion( 'newIdProducto',newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id string y descripcion tamaño 501.
    def testinsert_AccionIdStringDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*501
        result = tempAccion.insert_Accion( 'newIdProducto',newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion entero.
    def testinsert_AccionIdFloatDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 32
        result = tempAccion.insert_Accion( 43.32,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion float.
    def testinsert_AccionIdFloatDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 32.323
        result = tempAccion.insert_Accion( 43.32,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion None.
    def testinsert_AccionIdFloatDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( 43.32,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion tamaño 500.
    def testinsert_AccionIdFloatDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*500
        result = tempAccion.insert_Accion( 43.32,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion tamaño 501.
    def testinsert_AccionIdFloatDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*501
        result = tempAccion.insert_Accion( 43.32,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion entero.
    def testinsert_AccionIdNoneDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 34
        result = tempAccion.insert_Accion( None,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion float.
    def testinsert_AccionIdNoneDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 34.23
        result = tempAccion.insert_Accion( None,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion None.
    def testinsert_AccionIdNoneDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( None,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id None y descripcion 500.
    def testinsert_AccionIdNoneDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*500
        result = tempAccion.insert_Accion( None,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion 501.
    def testinsert_AccionIdNoneDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*501
        result = tempAccion.insert_Accion( None,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion entero.
    def testinsert_AccionIdGrantDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 34
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id Grande y descripcion float.
    def testinsert_AccionIdGrantDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 34.32
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion None.
    def testinsert_AccionIdGrantDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion 500.
    def testinsert_AccionIdGrantDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*500
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion 501.
    def testinsert_AccionIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*501
        result = tempAccion.insert_Accion( newIdProducto,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
 
     # Se insertara un accion con id Negativo y descripcion entero.
    def testinsert_AccionIdNegativeDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 34
        result = tempAccion.insert_Accion( -3,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id negativo y descripcion float.
    def testinsert_AccionIdNegativeDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 34.32
        result = tempAccion.insert_Accion( -3,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo y descripcion None.
    def testinsert_AccionIdNegativeDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( -3,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo y descripcion 500.
    def testinsert_AccionIdNegativeDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*500
        result = tempAccion.insert_Accion(-3,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo y descripcion 501.
    def testinsert_AccionIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        newDescripAccion = 'y'*501
        result = tempAccion.insert_Accion( -3 ,newDescripAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del accion a modificar existe en la base de datos de un elemento.
    def testmodify_AccionExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'accionX'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testmodify_AccionNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 20
        newDescripAccion = 'Esto sigue siendo una prueba'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del accion a modificar existe en la base de datos de varios accions 
    def testmodify_AccionIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(1,10,1):
            newIdAccion = indice
            newDescripAccion = 'Descripcion ' + str(indice)
            newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
            model.db.session.add(newAccion)
            model.db.session.commit()   
            
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'esto sigue siendo una prueva V2'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del accion a modificar no existe en la base de datos de varios accions 
    def testmodify_AccionIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(2,10,1):
            newIdAccion = indice
            newDescripAccion = 'Descripcion ' + str(indice)
            newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion ) 
            model.db.session.add(newAccion)
            model.db.session.commit()   
            
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'esto sigue siendo una prueva V2'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del accion a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_AccionIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'l'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del accion a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_AccionIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'y'*500
        result = tempAccion.modify_Accion(newIdProducto, idaccion, newDescripAccion )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del accion a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_AccionIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdAccion = 1
        newDescripAccion = 'z'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'z'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del accion a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_AccionIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdAccion = 1
        newDescripAccion = 'x'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del accion a modificar es un string.
    def testmodify_AccionIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
            
        tempAccion = clsAccion()
        idaccion = '1'
        newDescripAccion = 'Axx'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testmodify_AccionIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
           
        tempAccion = clsAccion()
        idaccion = -1
        newDescripAccion = 'accion de prueba'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del accion a modificar es un float.
    def testmodify_AccionIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
          
        tempAccion = clsAccion()
        idaccion = 1.0
        newDescripAccion = 'accion de prueba'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del accion a modificar es None.         
    def testmodify_AccionIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempAccion = clsAccion()
        idaccion = None
        newDescripAccion = 'accionPrueba'
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_AccionDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()   
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
             
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = ''
        result = tempAccion.modify_Accion(newIdProducto, idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es de longitud 501.    
    def testmodify_AccionDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
           
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
           
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 'r'*501
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el accion a modificar es un numero.
    def testmodify_AccionDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
            
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = 12345
        result = tempAccion.modify_Accion(newIdProducto, idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el accion a modificar es None. 
    def testmodify_AccionDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 1
        newDescripAccion = None
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es Entero y id string . 
    def testmodify_AccionIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        newDescripAccion = 1212
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es Float y id string . 
    def testmodify_AccionIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        newDescripAccion = 1212.23
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id string . 
    def testmodify_AccionIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        newDescripAccion = None
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 500 y id string . 
    def testmodify_AccionIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        newDescripAccion = 'y'*500
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id string . 
    def testmodify_AccionIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        newDescripAccion = 'y'*501
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño Entero y id float . 
    def testmodify_AccionIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        newDescripAccion = 23
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño Float y id float . 
    def testmodify_AccionIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        newDescripAccion = 23.23
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id float . 
    def testmodify_AccionIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        newDescripAccion = None
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el accion a modificar es tamaño 500 y id float . 
    def testmodify_AccionIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        newDescripAccion = 'y'*500
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id float . 
    def testmodify_AccionIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        newDescripAccion = 'y'*501
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es entero y id None . 
    def testmodify_AccionIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        newDescripAccion = 23
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es float y id None . 
    def testmodify_AccionIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        newDescripAccion = 23.23
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id None . 
    def testmodify_AccionIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        newDescripAccion = None
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 500 y id None . 
    def testmodify_AccionIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        newDescripAccion = 'y'*500
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id None . 
    def testmodify_AccionIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        newDescripAccion = 'y'*501
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el accion a modificar es Entero y id MAX . 
    def testmodify_AccionIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 2**31 -1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        newDescripAccion = 43
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es float y id MAX . 
    def testmodify_AccionIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 2**31 -1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        newDescripAccion = 43.323
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id MAX . 
    def testmodify_AccionIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 2**31 -1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        newDescripAccion = None
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 500 y id MAX . 
    def testmodify_AccionIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 2**31 -1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        newDescripAccion = 'y'*500
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id MAX . 
    def testmodify_AccionIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdAccion = 2**31 -1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdProducto,newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        newDescripAccion = 'y'*501
        result = tempAccion.modify_Accion( newIdProducto,idaccion, newDescripAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
