"""   UNIVERSIDAD SIMON BOLIVAR
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

sys.path.append('../')
from funcObjetivo import clsObjetivo



import unittest


class TestObjetivo(unittest.TestCase):
    
    # FUNCION AUXILIAR
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Historias ).delete()
        model.db.session.query( model.Actores ).delete()
        model.db.session.query( model.Enlaces ).delete()
        model.db.session.query( model.Objetivos ).delete()  # Se limpia la base de datos.
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
    
    # Test 1: Se crea el objeto clsObjetivo.
    def testObjectExist(self):
        tempObj = clsObjetivo()
        self.assertIsNotNone( tempObj )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Buscar el id de un objetivo que exista en la base de datos de un elemento. 
    def testBuscarIdObjetivoExist(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()

    # Buscar el id de un objetivo con base de datos vacia
    def testBuscarIdObjetivoNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1000
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un objetivo con base de datos un elemento y busqueda no exitosa
        
    def testBuscarIdObjetivoNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        self.vaciarBaseDeDatos()
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdObjetivo = 2
        nuevoDescripcionObjetivo = 'Esto es una prueba'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un objetivo con base de datos de varios elemento y busqueda no exitosa   
    def testBuscarIdObjetivoNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 5
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un objetivo con base de datos de varios elemento y busqueda exitosa   
    def testBuscarIdObjetivoExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 3
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del objetivo a buscar es un string.
    def testBuscarIdObjetivoString(self):
        self.vaciarBaseDeDatos()
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = '1'
        query = tempObjetivo.buscarId(idObjetivo )
        self.assertEqual(query,None)
        
        self.vaciarBaseDeDatos()
        
    # El id del objetivo a buscar es de tipo float.
    def testBuscarIdObjetivoFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1.01
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del objetivo a buscar es nulo.
    def testBuscarIdObjetivoNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del objetivo a buscar es negativo.
    def testBuscarIdObjetivoNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = -3
        query = tempObjetivo.buscarId( idObjetivo )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un objetivo con un elemento en la base de datos vacia.
    def testinsertarBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        nuevoIdObjetivo = 3
        nuevoDescripcionObjetivo = 'Esto es una prueba'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
        

        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un objetivo con la base de datos vacia.
    def testinsertarBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        

        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un objetivo con varios elementos en la base de datos.
    def testinsertarBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        for indice in range(5,10,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
            
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un objetivo cuyo tama�o es igual a 1.
    def testinsertarDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = '1'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un objetivo cuyo tama�o es igual a 500.
    def testinsertarDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un Objetivo cuyo tama�o es 0 (Cadena Vac�a).
    def testinsertarDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = ''
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuyo tama�o es de 501.
    def testinsertarDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una Objetivo cuya descripcion es un numero.
    def testinsertarDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 501
        result = tempObjetivo.insertar(nuevoIdProducto, nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya descripcion dada es None.
    def testinsertarDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya descripcion dada es Float.
    def testinsertarDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 0.54
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo cuya transversalidad dada es Float.
    def testinsertartransversalidadFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = "descripcion"
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0.3)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya transversalidad dada es None
    def testinsertartransversalidadNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = "descripcion"
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,None)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya transversalidad dada es String
    def testinsertartransversalidadString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = "descripcion"
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,"None")
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo cuya transversalidad dada es negativa
    def testinsertartransversalidadNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = "descripcion"
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,-3)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya transversalidad dada es 3
    def testinsertartransversalidadIsTres(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = "descripcion"
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,3)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #Se insertara un objetivo con id string
    def testinsertarIdString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'ola k ase'
        result = tempObjetivo.insertar( 'error',nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un objetivo con id Float
    def testinsertarIdFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.insertar(1.32,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                

    # Se insertara un Objetivo con id float.
    def testinsertarIdNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'None.. uff caiste'
        result = tempObjetivo.insertar( None,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id maximo.
    def testinsertarIdGrant(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'None.. uff caiste'
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo.
    def testinsertarIdNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'None.. uff caiste'
        result = tempObjetivo.insertar( -3,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion entero.
    def testinsertarIdStringDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 123
        result = tempObjetivo.insertar( 'nuevoIdProducto',nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion float.
    def testinsertarIdStringDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 23.23
        result = tempObjetivo.insertar( 'nuevoIdProducto',nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion None.
    def testinsertarIdStringDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.insertar( 'nuevoIdProducto',nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion tamaño 500.
    def testinsertarIdStringDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.insertar( 'nuevoIdProducto',nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id string y descripcion tamaño 501.
    def testinsertarIdStringDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.insertar( 'nuevoIdProducto',nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion entero.
    def testinsertarIdFloatDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 32
        result = tempObjetivo.insertar( 43.32,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion float.
    def testinsertarIdFloatDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 32.323
        result = tempObjetivo.insertar( 43.32,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion None.
    def testinsertarIdFloatDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.insertar( 43.32,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion tamaño 500.
    def testinsertarIdFloatDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.insertar( 43.32,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion tamaño 501.
    def testinsertarIdFloatDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.insertar( 43.32,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion entero.
    def testinsertarIdNoneDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 34
        result = tempObjetivo.insertar( None,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion float.
    def testinsertarIdNoneDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 34.23
        result = tempObjetivo.insertar( None,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion None.
    def testinsertarIdNoneDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.insertar( None,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id None y descripcion 500.
    def testinsertarIdNoneDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.insertar( None,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion 501.
    def testinsertarIdNoneDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.insertar( None,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion entero.
    def testinsertarIdGrantDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 34
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id Grande y descripcion float.
    def testinsertarIdGrantDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 34.32
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion None.
    def testinsertarIdGrantDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion 500.
    def testinsertarIdGrantDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion 501.
    def testinsertarIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.insertar( nuevoIdProducto,nuevoDescripcionObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
 
     # Se insertara un Objetivo con id Negativo y descripcion entero.
    def testinsertarIdNegativeDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 34
        result = tempObjetivo.insertar( -3,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id negativo y descripcion float.
    def testinsertarIdNegativeDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 34.32
        result = tempObjetivo.insertar( -3,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo y descripcion None.
    def testinsertarIdNegativeDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.insertar( -3,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo y descripcion 500.
    def testinsertarIdNegativeDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.insertar( -3,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo y descripcion 501.
    def testinsertarIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.insertar( -3 ,nuevoDescripcionObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del objetivo a modificar existe en la base de datos de un elemento.
    def testmodificarExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'ObjetivoX'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testmodificarNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 20
        nuevoDescripcionObjetivo = 'Esto sigue siendo una prueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del objetivo a modificar existe en la base de datos de varios objetivos 
    def testmodificarIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        for indice in range(1,10,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
            
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'esto sigue siendo una prueva V2'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del objetivo a modificar no existe en la base de datos de varios objetivos 
    def testmodificarIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        for indice in range(2,10,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
            
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'esto sigue siendo una prueva V2'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del objetivo a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodificarIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'l'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del objetivo a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodificarIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        model.db.session.query(model.Objetivos).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del objetivo a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodificarIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'z'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'z'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del objetivo a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodificarIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'x'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del objetivo a modificar es un string.
    def testmodificarIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempObjetivo = clsObjetivo()
        idObjetivo = '1'
        nuevoDescripcionObjetivo = 'Axx'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testmodificarIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
           
        tempObjetivo = clsObjetivo()
        idObjetivo = -1
        nuevoDescripcionObjetivo = 'Objetivo de prueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del objetivo a modificar es un float.
    def testmodificarIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 1.0
        nuevoDescripcionObjetivo = 'Objetivo de prueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del objetivo a modificar es None.         
    def testmodificarIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        nuevoDescripcionObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La transversalidad dada del objetivo a modificar es None.         
    def testmodificartransversalidadNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,None )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La transversalidad dada del objetivo a modificar es String         
    def testmodificartransversalidadString(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,"None" )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La transversalidad dada del objetivo a modificar es float        
    def testmodificartransversalidadFloat(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modificar(idObjetivo, nuevoDescripcionObjetivo,0.3 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La transversalidad dada del objetivo a modificar es negativa       
    def testmodificartransversalidadNegative(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modificar(idObjetivo, nuevoDescripcionObjetivo,-3 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La transversalidad dada del objetivo a modificar es tres      
    def testmodificartransversalidadIsTres(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,3 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodificarDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = ''
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es de longitud 501.    
    def testmodificarDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
           
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()
           
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 'r'*501
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el objetivo a modificar es un numero.
    def testmodificarDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = 12345
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el objetivo a modificar es None. 
    def testmodificarDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es Entero y id string . 
    def testmodificarIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        nuevoDescripcionObjetivo = 1212
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es Float y id string . 
    def testmodificarIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        nuevoDescripcionObjetivo = 1212.23
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id string . 
    def testmodificarIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id string . 
    def testmodificarIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id string . 
    def testmodificarIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño Entero y id float . 
    def testmodificarIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        nuevoDescripcionObjetivo = 23
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño Float y id float . 
    def testmodificarIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        nuevoDescripcionObjetivo = 23.23
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id float . 
    def testmodificarIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id float . 
    def testmodificarIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id float . 
    def testmodificarIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es entero y id None . 
    def testmodificarIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        nuevoDescripcionObjetivo = 23
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es float y id None . 
    def testmodificarIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        nuevoDescripcionObjetivo = 23.23
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id None . 
    def testmodificarIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id None . 
    def testmodificarIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id None . 
    def testmodificarIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el objetivo a modificar es Entero y id MAX . 
    def testmodificarIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 43
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es float y id MAX . 
    def testmodificarIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 43.323
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id MAX . 
    def testmodificarIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = None
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id MAX . 
    def testmodificarIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'y'*500
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id MAX . 
    def testmodificarIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto=model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()  
        
        nuevoIdObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'Esto es una prueba.'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 )  
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        nuevoDescripcionObjetivo = 'y'*501
        result = tempObjetivo.modificar( idObjetivo, nuevoDescripcionObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #.-------------------------------------------------------------------.
    # FUNCION ELIMINAR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Eliminar el id de un objetivo que exista en la base de datos de un elemento. 
    def testEliminarIdObjetivoExist(self):
        self.vaciarBaseDeDatos()

        idProducto=1
        self.insertarProducto(idProducto)
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdObjetivo = 1
        nuevoDescripcionObjetivo = 'Esto es una prueba'
        nuevoObjetivo = model.Objetivos( idProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo,0 ) 
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idobjetivo = 1
        query = tempObjetivo.eliminar(idobjetivo )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()

    # Eliminar el id de un objetivo con base de datos vacia
    def testEliminarIdObjetivoNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempObjetivo = clsObjetivo()
        idobjetivo = 1000
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()

        
    # Eliminar el id de un objetivo con base de datos un elemento y busqueda no exitosa
        
    def testEliminarIdObjetivoNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdObjetivo = 2
        nuevoDescripcionObjetivo = 'Esto es una prueba'
        nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo ,0) 
        model.db.session.add(nuevoObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idobjetivo = 1
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
        
    # Eliminar el id de un objetivo con base de datos de varios elemento y busqueda no exitosa   
    def testEliminarIdObjetivoNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo ,0) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idobjetivo = 5
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
          
    # Eliminar el id de un objetivo con base de datos de varios elemento y busqueda exitosa   
    def testEliminarIdObjetivoExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdObjetivo = indice
            nuevoDescripcionObjetivo = 'Descripcion ' + str(indice)
            nuevoObjetivo = model.Objetivos( nuevoIdProducto,nuevoIdObjetivo, nuevoDescripcionObjetivo ,0) 
            model.db.session.add(nuevoObjetivo)
            model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idobjetivo = 3
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del objetivo a Eliminar es un string.
    def testEliminarIdObjetivoString(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
 
        
        tempObjetivo = clsObjetivo()
        idobjetivo = '1'
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)
        
        self.vaciarBaseDeDatos()
        
    # El id del objetivo a Eliminar es de tipo float.
    def testEliminarIdObjetivoFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempObjetivo = clsObjetivo()
        idobjetivo = 1.01
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del objetivo a Eliminar es nulo.
    def testEliminarIdObjetivoNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempObjetivo = clsObjetivo()
        idobjetivo = None
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del objetivo a Eliminar es negativo.
    def testEliminarIdObjetivoNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempObjetivo = clsObjetivo()
        idobjetivo = -3
        query = tempObjetivo.eliminar( idobjetivo )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------. 
    #.-------------------------------------------------------------------.