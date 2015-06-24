"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcProducto.py"
    
"""

#----------------------------------------------------------------------------

# Librerias a utilizar
import os
import sys

# PATH que permite utilizar el "model.py"
sys.path.append('../../../')
import model

sys.path.append('../')
from funcProducto import clsProducto



import unittest


class TestProducto(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Productos ).delete() 
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsProducto.
    def testObjectExist(self):
        tempProducto = clsProducto()
        self.assertIsNotNone( tempProducto )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Buscar el id de un producto que exista en la base de datos de un elemento. 
    def testBuscarIdProductoExist(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertIsNotNone( query )
        
        self.vaciarBaseDeDatos()

    # Buscar el id de un productocon base de datos vacia
    
    def testBuscarIdProductoNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        nuevoIdProducto= 1000
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un producto con base de datos un elemento y busqueda no exitosa
        
    def testBuscarIdProductoNotExistOneElemento(self):
        self.vaciarBaseDeDatos()
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= 2
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un producto con base de datos de varios elemento y busqueda no exitosa   
    
    def testBuscarIdProductoNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
     
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdProducto = indice
            nuevoDescripcionProducto=' Descripcion Producto.. ' + str(indice)
            nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
            model.db.session.add(nuevoProducto)
            model.db.session.commit()   
        
        tempProducto = clsProducto()
        nuevoIdProducto= 5
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un producto con base de datos de varios elementos y busqueda exitosa   
    def testBuscarIdProductoExistVariosElementos(self):
        self.vaciarBaseDeDatos()  

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdProducto = indice
            nuevoDescripcionProducto=' Descripcion Producto.. ' + str(indice)
            nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
            model.db.session.add(nuevoProducto)
            model.db.session.commit()   
        
        tempProducto = clsProducto()
        nuevoIdProducto= 3
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del producto a buscar es un string.
    def testBuscarIdProductoString(self):
        self.vaciarBaseDeDatos()
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= '1'
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)
        
        self.vaciarBaseDeDatos()
        
    # El id del producto a buscar es de tipo float.
    def testBuscarIdProductoFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= 1.01
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del productoa buscar es nulo.
    def testBuscarIdProductoNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= None
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del productoa buscar es negativo.
    def testBuscarIdProductoNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= -3
        query = tempProducto.buscarId(nuevoIdProducto)
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un producto con un elemento en la base de datos.
    def testInsertarProductoBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 2
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un producto con la base de datos vacia.
    def testInsertarProductoBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertTrue(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un producto con varios elementos en la base de datos.
    def testInsertarProductoBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()

        
        for indice in range(5,10,1):
            nuevoIdProducto= indice
            nuevoDescripcionProducto= 'Descripcion ' + str(indice)
            nuevoProducto= model.Productos( nuevoIdProducto,"Producto", nuevoDescripcionProducto,1) 
            model.db.session.add(nuevoProducto)
            model.db.session.commit()   
            
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un productocuyo tama�o es igual a 1.
    def testInsertarProductoDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= '1'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un producto cuyo tama�o es igual a 500.
    def testInsertarProductoDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempProducto = clsProducto()
        nuevoDescripcionProducto='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un producto cuyo tama�o es 0 (Cadena Vac�a).
    def testInsertarProductoDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= ''
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un productocuyo tama�o es de 501.
    def testInsertarProductoDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una producto cuya descripcion es un numero.
    def testInsertarProductoDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 501
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un productocuya descripcion dada es None.
    def testInsertarProductoDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        tempProducto = clsProducto()
        nuevoDescripcionProducto= None
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un productocuya descripcion dada es Float.
    def testInsertarProductoDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 0.54
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un producto con escala string.
    def testInsertarProductoEscalaString(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,"error")
        self.assertFalse(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Insertar un producto con escala None
    def testInsertarProductoEscalaNone(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,None)
        self.assertFalse(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un producto con escala 3
    def testInsertarProductoEscalaTres(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,3)
        self.assertFalse(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un producto con escala 0
    def testInsertarProductoEscalaZero(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,0)
        self.assertFalse(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Insertar un producto con escala float
    def testInsertarProductoEscalaFloat(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'producto2.0'
        result = tempProducto.insertar("Producto Nuevo",nuevoDescripcionProducto,0.32)
        self.assertFalse(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del producto a modificar existe en la base de datos de un elemento.
    def testModificarProductoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoDescripcionProducto= 'ObjetivoX'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del producto a modificar existe en la base de datos de varios elementos 
    def testModificarProductoIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
       
        for indice in range(1,10,1):
            nuevoIdProducto= indice
            nuevoDescripcionProducto= 'Descripcion ' + str(indice)
            nuevoProducto= model.Productos( nuevoIdProducto,"Producto", nuevoDescripcionProducto,1) 
            model.db.session.add(nuevoProducto)
            model.db.session.commit()   
            
        tempProducto = clsProducto()
        nuevoIdProducto= 3
        nuevoDescripcionProducto= 'esto sigue siendo una prueva V2'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    

    
    #  El id del productoa modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testModificarProductoIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos( nuevoIdProducto,"Producto", nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'l'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del productoa modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testModificarProductoIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'y'*500
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        model.db.session.query(model.Productos).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del productoa modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testModificarProductoIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'z'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'z'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del productoa modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testModificarProductoIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
               
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    
    # la escala del producto a modificar es un string.
    def testModificarProductoEscalaString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Axx'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,"1")
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # la escala del producto a modificar es un None.
    def testModificarProductoEscalaNone(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Axx'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,None)
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # la escala del producto a modificar es un Float.
    def testModificarProductoEscalaFloat(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Axx'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,3.32)
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
    
    # la escala del producto a modificar es un cero.
    def testModificarProductoEscalaZero(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Axx'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,0)
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
    # la escala del producto a modificar es un tres.
    def testModificarProductoEscalaTres(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Axx'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,3)
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
    # El id dado del producto a modificar es un string.
    def testModificarProductoIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        nuevoIdProducto= '1'
        nuevoDescripcionProducto= 'Axx'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testModificarProductoIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
           
        tempProducto = clsProducto()
        nuevoIdProducto= -1
        nuevoDescripcionProducto= 'productode prueba'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del productoa modificar es un float.
    def testModificarProductoIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
          
        tempProducto = clsProducto()
        nuevoIdProducto= 1.0
        nuevoDescripcionProducto= 'productode prueba'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del productoa modificar es None.         
    def testModificarProductoIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        nuevoDescripcionProducto=' Descripcion Producto.. '
        nuevoProducto = model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit() 
             
        tempProducto = clsProducto()
        nuevoIdProducto= None
        nuevoDescripcionProducto= 'ObjetivoPrueba'
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testModificarProductoDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()
             
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= ''
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es de longitud 501.    
    def testModificarProductoDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
           
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()
           
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'r'*501
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el productoa modificar es un numero.
    def testModificarProductoDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
            
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 12345
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el productoa modificar es None. 
    def testModificarProductoDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 1
        nuevoDescripcionProducto= None
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es Entero y id string . 
    def testModificarProductoIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 'malo'
        nuevoDescripcionProducto= 1212
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es Float y id string . 
    def testModificarProductoIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 'malo'
        nuevoDescripcionProducto= 1212.23
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id string . 
    def testModificarProductoIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 'malo'
        nuevoDescripcionProducto= None
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 500 y id string . 
    def testModificarProductoIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 'malo'
        nuevoDescripcionProducto= 'y'*500
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 501 y id string . 
    def testModificarProductoIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 'malo'
        nuevoDescripcionProducto= 'y'*501
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño Entero y id float . 
    def testModificarProductoIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 23.23
        nuevoDescripcionProducto= 23
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño Float y id float . 
    def testModificarProductoIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 23.23
        nuevoDescripcionProducto= 23.23
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id float . 
    def testModificarProductoIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 23.23
        nuevoDescripcionProducto= None
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el productoa modificar es tamaño 500 y id float . 
    def testModificarProductoIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 23.23
        nuevoDescripcionProducto= 'y'*500
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 501 y id float . 
    def testModificarProductoIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 23.23
        nuevoDescripcionProducto= 'y'*501
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es entero y id None . 
    def testModificarProductoIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= None
        nuevoDescripcionProducto= 23
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es float y id None . 
    def testModificarProductoIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= None
        nuevoDescripcionProducto= 23.23
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id None . 
    def testModificarProductoIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= None
        nuevoDescripcionProducto= None
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 500 y id None . 
    def testModificarProductoIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= None
        nuevoDescripcionProducto= 'y'*500
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 501 y id None . 
    def testModificarProductoIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
     
        nuevoIdProducto= 1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= None
        nuevoDescripcionProducto= 'y'*501
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el productoa modificar es Entero y id MAX . 
    def testModificarProductoIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 43
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es float y id MAX . 
    def testModificarProductoIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1) 
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 43.323
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id MAX . 
    def testModificarProductoIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
      
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= None
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 500 y id MAX . 
    def testModificarProductoIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
      
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'y'*500
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el producto a modificar es tamaño 501 y id MAX . 
    def testModificarProductoIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
      
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'Esto es una prueba.'
        nuevoProducto= model.Productos(nuevoIdProducto,"producto",nuevoDescripcionProducto,1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        nuevoIdProducto= 2**31 -1
        nuevoDescripcionProducto= 'y'*501
        result = tempProducto.modificar(nuevoIdProducto,"Nuevo Nombre",nuevoDescripcionProducto,1)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #.-------------------------------------------------------------------.
    #.-------------------------------------------------------------------.