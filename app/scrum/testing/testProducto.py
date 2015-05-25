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

# PATH que permite utilizar al modulo "dpt.py"
sys.path.append('../')
from funcProducto import clsProducto

import unittest

class TestProducto(unittest.TestCase):

    #.-----------------------------------------------------.
    # VERIFICACION DE LA CLASE

    # Test 1: Se crea el objeto clsProducto
    def testObjectExist(self):
        tempProducto = clsProducto()
        self.assertIsNone( tempProducto )
        model.db.session.query( model.Pila ).delete() # Se limpia la base de datos

    #.-----------------------------------------------------.
    # FUNCION BUSCAR

    ### CASOS VALIDOS (Casos Interiores).

    #Test 2: Buscar el iid de un producto que exista

    def testfind_idProductExist(self):
        #Se inserta un elemento valido en la base de datos
        newIdProducto = 1
        newProducto = model.Pila(newIdProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()

        tempProducto = clsProducto
        idProducto = 1
        query = tempProducto.find_idProducto( idProducto )
        self.assertIsNone(query[0])
        model.db.session.query( model.Pila ).delete() # Se limpia la base de datos

    # Test 3: Buscar el id de un Producto que no existe
    def testfind_idProductoNotExist(self):
        tempProducto = clsProducto()
        idProducto = 1000
        query = tempProducto.find_idProducto( idProducto )
        self.assertEqual(query,[])

    ### CASOS INVALIDOS ( Casos Malicia )

    # Test 4: El id del Producto a buscar es un string
    def testfind_idProductoString(self):
        tempProducto = clsProducto()
        idProducto = '1'
        query = tempProducto.find_idProducto( idProducto )
        self.assertEqual(query,[])
    
    # Test 5: El id del Producto a buscar es de tipo float.
    def testfind_idProductoFloat(self):
        tempProducto = clsProducto()
        idProducto = 1.01
        query = tempProducto.find_idProducto( idProducto )
        self.assertEqual(query,[])  

    # Test 6: El id del producto a buscar es nulo.
    def testfind_idProductoNone(self):
        tempProducto = clsProducto()
        idProducto = None
        query = tempProducto.find_idProducto( idProducto )
        self.assertEqual(query,[])

    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Insertar un producto
    def testinsert_producto(self):
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        newDescripProducto = 'Producto 2.0'
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertTrue(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
           
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 8: Se insertara un producto cuyo tama�o es igual a 1.
    def testinsert_productoLen1(self):
        tempProducto = clsProducto()
        newDescripProducto = '1'
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertTrue(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.

    # Test 9: Se insertara un producto cuyo tama�o es igual a 500.
    def testinsert_productoLen500(self):
        tempProducto = clsProducto()
        newDescripProducto ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertTrue(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 10: Se insertara un producto cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_productoLen0(self):
        tempProducto = clsProducto()
        newDescripProducto = ''
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertFalse(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.

    # Test 11: Se insertara un producto cuyo tama�o es de 501.
    def testinsert_productoLen501(self):
        tempProducto = clsProducto()
        newDescripProducto = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu,'
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertFalse(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.

    # Test 12: Se insertara un producto cuya descripcion es un numero.
    def testinsert_productoNumber(self):
        tempProducto = clsProducto()
        newDescripProducto = 501
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertFalse(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.

    # Test 13: Se insertara un producto cuya descripcion dada es None.
    def testinsert_productoNone(self):
        tempProducto = clsProducto()
        newDescripProducto = None
        result = tempProducto.insert_Producto( newDescripProducto )
        self.assertFalse(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.

 #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 14: El id del producto a modificar existe en la base de datos.
    def testmodify_productoExist(self):
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 'ProductoX'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertTrue( result ) 
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.        

    # Test 15: El id del producto a modificar no existe en la base de datos.
    def testmodify_productoNoExist(self):
        tempProducto = clsProducto()
        idProducto = 20
        newDescripProducto = 'Esto sigue siendo una prueba'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result ) 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 16: El id del producto a modificar existe en la base de datos y su
    #          valor es igual a 1. 
    def testmodify_productoIdExistIqual1(self):
        
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        

        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 'esto sigue siendo una prueva V2'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertTrue( result ) 
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos. 

    
    # Test 17: El id del producto a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_productoIdExistNewDescripLen1(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 'l'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertTrue(result)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.   
    
    # Test 18: El id deproducto a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_productoIdExistNewDescripLen500(self):
        
        
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 'y'*500
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        
    
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 19: El id del producto a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_productoIdExistIqual1NewDescripLen1(self):
        newIdProducto = 1
        newDescripProducto = 'z'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 'z'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertTrue( result )
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos. 
    
    # Test 20: El id del producto a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_productoIdExistIqual1NewDescripLen500(self):
        
        newIdProducto = 1
        newDescripProducto = 'x'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertTrue( result ) 
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.

### CASOS INVALIDOS( Casos Malicia )
    # Test 21: El id dado del producto a modificar es un string.
    def testmodify_productoIdString(self):        
        tempProducto = clsProducto()
        idProducto = '1'
        newDescripProducto = 'Axx'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )    
        
    # Test 22: El id dado del producto a modificar es un numero negativo.    
    def testmodify_productoIdNegative(self):        
        tempProducto = clsProducto()
        idProducto = -1
        newDescripProducto = 'producto de prueba'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )   

    # Test 23: El id dado del producto a modificar es un float.
    def testmodify_productoIdFloat(self):        
        tempProducto = clsProducto()
        idProducto = 1.0
        newDescripProducto = 'producto de prueba'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )   
        
    # Test 24: El id dado del producto a modificar es None.         
    def testmodify_productoIdNone(self):        
        tempProducto = clsProducto()
        idProducto = None
        newDescripProducto = 'productoPrueba'
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )   
    
    # Test 25: La nueva descripcion para el producto a modificar es un string vacio.
    def testmodify_productoDescripIsEmpty(self):   
        
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
             
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = ''
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.    
        
    # Test 26: La nueva descripci�n para el producto a modificar es de longitud 501.    
    def testmodify_productoDescripLen501(self):     
        
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
           
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 'r'*501
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.    

    # Test 27: La nueva descripci�n para el producto a modificar es un numero.
    def testmodify_productoDescripIsNumber(self):        
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = 12345
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.    
        
    # Test 28: La nueva descripci�n para el producto a modificar es None. 
    def testmodify_productoDescripNone(self):   
        
        newIdProducto = 1
        newDescripProducto = 'Esto es una prueba.'
        newProducto = model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        idProducto = 1
        newDescripProducto = None
        result = tempProducto.modify_Producto( idProducto, newDescripProducto )
        self.assertFalse( result )
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.    

    #.-------------------------------------------------------------------.  