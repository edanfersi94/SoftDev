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
        model.db.session.query( model.Historias ).delete()
        model.db.session.query( model.Objetivos ).delete()
        model.db.session.query( model.Acciones ).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Productos ).delete() 
    
    def insertarProducto(self, nuevoIdProducto):
        nuevoNombreProducto='Nombre Producto'
        nuevoEscalaProducto= 1
        nuevoDescripcionProducto= 'Descripcion Producto'
        nuevoProducto = model.Productos(nuevoIdProducto,nuevoNombreProducto,nuevoDescripcionProducto,nuevoEscalaProducto)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
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
    def testBuscarIdAccionExist(self):
        self.vaciarBaseDeDatos()

        idProducto=1
        self.insertarProducto(idProducto)
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba'
        nuevoAccion = model.Acciones( idProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 1
        query = tempAccion.buscarId(idaccion )
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()

    # Buscar el id de un accion con base de datos vacia
    def testBuscarIdAccionNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = 1000
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un accion con base de datos un elemento y busqueda no exitosa
        
    def testBuscarIdAccionNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdAccion = 2
        nuevoDescripcionAccion = 'Esto es una prueba'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 1
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un accion con base de datos de varios elemento y busqueda no exitosa   
    def testBuscarIdAccionNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 5
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un accion con base de datos de varios elemento y busqueda exitosa   
    def testBuscarIdAccionExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 3
        query = tempAccion.buscarId( idaccion )
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del accion a buscar es un string.
    def testBuscarIdAccionString(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
 
        
        tempAccion = clsAccion()
        idaccion = '1'
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)
        
        self.vaciarBaseDeDatos()
        
    # El id del accion a buscar es de tipo float.
    def testBuscarIdAccionFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = 1.01
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del accion a buscar es nulo.
    def testBuscarIdAccionNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempAccion = clsAccion()
        idaccion = None
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del accion a buscar es negativo.
    def testBuscarIdAccionNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = -3
        query = tempAccion.buscarId( idaccion )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un accion con un elemento en la base de datos vacia.
    def testInsertarAccionBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 3
        nuevoDescripcionAccion = 'Esto es una prueba'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
        

        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'accion 2.0'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un accion con la base de datos vacia.
    def testInsertarAccionBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'accion 2.0'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un accion con varios elementos en la base de datos.
    def testInsertarAccionBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        for indice in range(5,10,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
            
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'accion 2.0'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un accion cuyo tama�o es igual a 1.
    def testInsertarAccionDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = '1'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un accion cuyo tama�o es igual a 500.
    def testInsertarAccionDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un accion cuyo tama�o es 0 (Cadena Vac�a).
    def testInsertarAccionDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = ''
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion cuyo tama�o es de 501.
    def testInsertarAccionDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una accion cuya descripcion es un numero.
    def testInsertarAccionDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 501
        result = tempAccion.insertar(nuevoIdProducto, nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion cuya descripcion dada es None.
    def testInsertarAccionDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = None
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion cuya descripcion dada es Float.
    def testInsertarAccionDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 0.54
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #Se insertara un accion con id string
    def testInsertarAccionIdString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'ola k ase'
        result = tempAccion.insertar( 'error',nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un accion con id Float
    def testInsertarAccionIdFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.insertar(1.32,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                

    # Se insertara un accion con id float.
    def testInsertarAccionIdNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'None.. uff caiste'
        result = tempAccion.insertar( None,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id maximo.
    def testInsertarAccionIdGrant(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'None.. uff caiste'
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo.
    def testInsertarAccionIdNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'None.. uff caiste'
        result = tempAccion.insertar(-3,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion entero.
    def testInsertarAccionIdStringDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 123
        result = tempAccion.insertar( 'nuevoIdProducto',nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion float.
    def testInsertarAccionIdStringDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 23.23
        result = tempAccion.insertar( 'nuevoIdProducto',nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion None.
    def testInsertarAccionIdStringDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = None
        result = tempAccion.insertar( 'nuevoIdProducto',nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id string y descripcion tamaño 500.
    def testInsertarAccionIdStringDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.insertar( 'nuevoIdProducto',nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id string y descripcion tamaño 501.
    def testInsertarAccionIdStringDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.insertar( 'nuevoIdProducto',nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion entero.
    def testInsertarAccionIdFloatDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 32
        result = tempAccion.insertar( 43.32,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion float.
    def testInsertarAccionIdFloatDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 32.323
        result = tempAccion.insertar( 43.32,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion None.
    def testInsertarAccionIdFloatDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = None
        result = tempAccion.insertar( 43.32,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion tamaño 500.
    def testInsertarAccionIdFloatDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.insertar( 43.32,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id float y descripcion tamaño 501.
    def testInsertarAccionIdFloatDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.insertar( 43.32,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion entero.
    def testInsertarAccionIdNoneDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 34
        result = tempAccion.insertar( None,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion float.
    def testInsertarAccionIdNoneDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 34.23
        result = tempAccion.insertar( None,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion None.
    def testInsertarAccionIdNoneDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = None
        result = tempAccion.insertar( None,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id None y descripcion 500.
    def testInsertarAccionIdNoneDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.insertar( None,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id None y descripcion 501.
    def testInsertarAccionIdNoneDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.insertar( None,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion entero.
    def testInsertarAccionIdGrantDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 34
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id Grande y descripcion float.
    def testInsertarAccionIdGrantDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 34.32
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion None.
    def testInsertarAccionIdGrantDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = None
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion 500.
    def testInsertarAccionIdGrantDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id Grande y descripcion 501.
    def testInsertarAccionIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.insertar( nuevoIdProducto,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
 
     # Se insertara un accion con id Negativo y descripcion entero.
    def testInsertarAccionIdNegativeDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 34
        result = tempAccion.insertar( -3,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un accion con id negativo y descripcion float.
    def testInsertarAccionIdNegativeDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 34.32
        result = tempAccion.insertar( -3,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo y descripcion None.
    def testInsertarAccionIdNegativeDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = None
        result = tempAccion.insertar( -3,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo y descripcion 500.
    def testInsertarAccionIdNegativeDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.insertar(-3,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un accion con id negativo y descripcion 501.
    def testInsertarAccionIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.insertar( -3 ,nuevoDescripcionAccion )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del accion a modificar existe en la base de datos de un elemento.
    def testModificarAccionExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'accionX'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testModificarAccionNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = 20
        nuevoDescripcionAccion = 'Esto sigue siendo una prueba'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del accion a modificar existe en la base de datos de varios accions 
    def testModificarAccionIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        for indice in range(1,10,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
            
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'esto sigue siendo una prueva V2'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del accion a modificar no existe en la base de datos de varios accions 
    def testModificarAccionIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        for indice in range(2,10,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
            
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'esto sigue siendo una prueva V2'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del accion a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testModificarAccionIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'l'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del accion a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testModificarAccionIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del accion a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testModificarAccionIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'z'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'z'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del accion a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testModificarAccionIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'x'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del accion a modificar es un string.
    def testModificarAccionIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
            
        tempAccion = clsAccion()
        idaccion = '1'
        nuevoDescripcionAccion = 'Axx'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testModificarAccionIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
           
        tempAccion = clsAccion()
        idaccion = -1
        nuevoDescripcionAccion = 'accion de prueba'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del accion a modificar es un float.
    def testModificarAccionIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
          
        tempAccion = clsAccion()
        idaccion = 1.0
        nuevoDescripcionAccion = 'accion de prueba'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del accion a modificar es None.         
    def testModificarAccionIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
             
        tempAccion = clsAccion()
        idaccion = None
        nuevoDescripcionAccion = 'accionPrueba'
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testModificarAccionDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()
             
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = ''
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es de longitud 501.    
    def testModificarAccionDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
           
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()
           
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 'r'*501
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el accion a modificar es un numero.
    def testModificarAccionDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
            
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()
        
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = 12345
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el accion a modificar es None. 
    def testModificarAccionDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 1
        nuevoDescripcionAccion = None
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es Entero y id string . 
    def testModificarAccionIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        nuevoDescripcionAccion = 1212
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es Float y id string . 
    def testModificarAccionIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        nuevoDescripcionAccion = 1212.23
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id string . 
    def testModificarAccionIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        nuevoDescripcionAccion = None
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 500 y id string . 
    def testModificarAccionIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id string . 
    def testModificarAccionIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 'malo'
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño Entero y id float . 
    def testModificarAccionIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        nuevoDescripcionAccion = 23
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño Float y id float . 
    def testModificarAccionIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        nuevoDescripcionAccion = 23.23
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id float . 
    def testModificarAccionIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        nuevoDescripcionAccion = None
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el accion a modificar es tamaño 500 y id float . 
    def testModificarAccionIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id float . 
    def testModificarAccionIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 23.23
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es entero y id None . 
    def testModificarAccionIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        nuevoDescripcionAccion = 23
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es float y id None . 
    def testModificarAccionIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        nuevoDescripcionAccion = 23.23
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id None . 
    def testModificarAccionIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        nuevoDescripcionAccion = None
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 500 y id None . 
    def testModificarAccionIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id None . 
    def testModificarAccionIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = None
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el accion a modificar es Entero y id MAX . 
    def testModificarAccionIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        nuevoIdAccion = 2**31 -1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        nuevoDescripcionAccion = 43
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es float y id MAX . 
    def testModificarAccionIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 2**31 -1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        nuevoDescripcionAccion = 43.323
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es None y id MAX . 
    def testModificarAccionIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        nuevoIdAccion = 2**31 -1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        nuevoDescripcionAccion = None
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 500 y id MAX . 
    def testModificarAccionIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 2**31 -1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        idaccion = 2**31 -1
        nuevoDescripcionAccion = 'y'*500
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el accion a modificar es tamaño 501 y id MAX . 
    def testModificarAccionIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdAccion = 2**31 -1
        nuevoDescripcionAccion = 'Esto es una prueba.'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
          
        tempAccion = clsAccion()
        

        idaccion = 2**31 -1
        nuevoDescripcionAccion = 'y'*501
        result = tempAccion.modificar( idaccion, nuevoDescripcionAccion )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #.-------------------------------------------------------------------.  
    # FUNCION ELIMINAR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Eliminar el id de un accion que exista en la base de datos de un elemento. 
    def testEliminarIdAccionExist(self):
        self.vaciarBaseDeDatos()

        idProducto=1
        self.insertarProducto(idProducto)
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdAccion = 1
        nuevoDescripcionAccion = 'Esto es una prueba'
        nuevoAccion = model.Acciones( idProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 1
        query = tempAccion.eliminar(idaccion )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()

    # Eliminar el id de un accion con base de datos vacia
    def testEliminarIdAccionNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = 1000
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()

        
    # Eliminar el id de un accion con base de datos un elemento y busqueda no exitosa
        
    def testEliminarIdAccionNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdAccion = 2
        nuevoDescripcionAccion = 'Esto es una prueba'
        nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
        model.db.session.add(nuevoAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 1
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
        
    # Eliminar el id de un accion con base de datos de varios elemento y busqueda no exitosa   
    def testEliminarIdAccionNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 5
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
          
    # Eliminar el id de un accion con base de datos de varios elemento y busqueda exitosa   
    def testEliminarIdAccionExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdAccion = indice
            nuevoDescripcionAccion = 'Descripcion ' + str(indice)
            nuevoAccion = model.Acciones( nuevoIdProducto,nuevoIdAccion, nuevoDescripcionAccion ) 
            model.db.session.add(nuevoAccion)
            model.db.session.commit()   
        
        tempAccion = clsAccion()
        idaccion = 3
        query = tempAccion.eliminar( idaccion )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del accion a Eliminar es un string.
    def testEliminarIdAccionString(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
 
        
        tempAccion = clsAccion()
        idaccion = '1'
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)
        
        self.vaciarBaseDeDatos()
        
    # El id del accion a Eliminar es de tipo float.
    def testEliminarIdAccionFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = 1.01
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del accion a Eliminar es nulo.
    def testEliminarIdAccionNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempAccion = clsAccion()
        idaccion = None
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del accion a Eliminar es negativo.
    def testEliminarIdAccionNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempAccion = clsAccion()
        idaccion = -3
        query = tempAccion.eliminar( idaccion )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
        