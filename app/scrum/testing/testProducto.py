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
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Pila ).delete() 
    
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
    def testfind_idProductoExist(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= 1
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertIsNotNone( query[0] )
        
        self.vaciarBaseDeDatos()

    # Buscar el id de un productocon base de datos vacia
    
    def testfind_idProductoNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        newIdProducto= 1000
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un producto con base de datos un elemento y busqueda no exitosa
        
    def testfind_idProductoNotExistOneElemento(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= 2
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un producto con base de datos de varios elemento y busqueda no exitosa   
    
    def testfind_idProductoNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
     
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdProducto = indice
            newDescripProducto=' Descripcion Producto.. ' + str(indice)
            newProducto = model.Pila(newIdProducto,newDescripProducto)
            model.db.session.add(newProducto)
            model.db.session.commit()   
        
        tempProducto = clsProducto()
        newIdProducto= 5
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un producto con base de datos de varios elementos y busqueda exitosa   
    def testfind_idProductoExistVariosElementos(self):
        self.vaciarBaseDeDatos()  

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdProducto = indice
            newDescripProducto=' Descripcion Producto.. ' + str(indice)
            newProducto = model.Pila(newIdProducto,newDescripProducto)
            model.db.session.add(newProducto)
            model.db.session.commit()   
        
        tempProducto = clsProducto()
        newIdProducto= 3
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del producto a buscar es un string.
    def testfind_idProductoString(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= '1'
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])
        
        self.vaciarBaseDeDatos()
        
    # El id del producto a buscar es de tipo float.
    def testfind_idProductoFloat(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= 1.01
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del productoa buscar es nulo.
    def testfind_idProductoNone(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= None
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del productoa buscar es negativo.
    def testfind_idProductoNegative(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= -3
        query = tempProducto.find_idProducto(newIdProducto)
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un producto con un elemento en la base de datos.
    def testinsert_ProductoBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 2
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newDescripProducto= 'producto2.0'
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un producto con la base de datos vacia.
    def testinsert_ProductoBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        newDescripProducto= 'producto2.0'
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertTrue(result[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un producto con varios elementos en la base de datos.
    def testinsert_ProductoBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()

        
        for indice in range(5,10,1):
            newIdProducto= indice
            newDescripProducto= 'Descripcion ' + str(indice)
            newProducto= model.Pila( newIdProducto, newDescripProducto) 
            model.db.session.add(newProducto)
            model.db.session.commit()   
            
        tempProducto = clsProducto()
        newDescripProducto= 'producto2.0'
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un productocuyo tama�o es igual a 1.
    def testinsert_ProductoDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        newDescripProducto= '1'
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un producto cuyo tama�o es igual a 500.
    def testinsert_ProductoDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempProducto = clsProducto()
        newDescripProducto='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertTrue(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un producto cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_ProductoDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        newDescripProducto= ''
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un productocuyo tama�o es de 501.
    def testinsert_ProductoDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempProducto = clsProducto()
        newDescripProducto= 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una producto cuya descripcion es un numero.
    def testinsert_ProductoDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        newDescripProducto= 501
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un productocuya descripcion dada es None.
    def testinsert_ProductoDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        tempProducto = clsProducto()
        newDescripProducto= None
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un productocuya descripcion dada es Float.
    def testinsert_ProductoDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempProducto = clsProducto()
        newDescripProducto= 0.54
        result = tempProducto.insert_Producto(newDescripProducto)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del producto a modificar existe en la base de datos de un elemento.
    def testmodify_ProductoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newDescripProducto= 'ObjetivoX'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testmodify_ProductoNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempProducto = clsProducto()
        newIdProducto= 20
        newDescripProducto= 'Esto sigue siendo una prueba'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del producto a modificar existe en la base de datos de varios elementos 
    def testmodify_ProductoIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
       
        for indice in range(1,10,1):
            newIdProducto= indice
            newDescripProducto= 'Descripcion ' + str(indice)
            newProducto= model.Pila( newIdProducto, newDescripProducto) 
            model.db.session.add(newProducto)
            model.db.session.commit()   
            
        tempProducto = clsProducto()
        newIdProducto= 3
        newDescripProducto= 'esto sigue siendo una prueva V2'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del producto a modificar no existe en la base de datos de varios productos
    def testmodify_ProductoIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. d
        
        for indice in range(2,10,1):
            newIdProducto= indice
            newDescripProducto= 'Descripcion ' + str(indice)
            newProducto= model.Pila(newIdProducto, newDescripProducto) 
            model.db.session.add(newProducto)
            model.db.session.commit()   
            
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= 'esto sigue siendo una prueva V2'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del productoa modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_ProductoIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= 'l'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del productoa modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_ProductoIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= 'y'*500
        result = tempProducto.modify_Producto(newIdProducto, newDescripProducto)
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del productoa modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_ProductoIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'z'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= 'z'
        result = tempProducto.modify_Producto( newIdProducto, newDescripProducto)
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del productoa modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_ProductoIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
               
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del producto a modificar es un string.
    def testmodify_ProductoIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
            
        tempProducto = clsProducto()
        newIdProducto= '1'
        newDescripProducto= 'Axx'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testmodify_ProductoIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
           
        tempProducto = clsProducto()
        newIdProducto= -1
        newDescripProducto= 'productode prueba'
        result = tempProducto.modify_Producto( newIdProducto, newDescripProducto)
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del productoa modificar es un float.
    def testmodify_ProductoIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
          
        tempProducto = clsProducto()
        newIdProducto= 1.0
        newDescripProducto= 'productode prueba'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del productoa modificar es None.         
    def testmodify_ProductoIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempProducto = clsProducto()
        newIdProducto= None
        newDescripProducto= 'ObjetivoPrueba'
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_ProductoDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
             
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= ''
        result = tempProducto.modify_Producto(newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es de longitud 501.    
    def testmodify_ProductoDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
           
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
           
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= 'r'*501
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el productoa modificar es un numero.
    def testmodify_ProductoDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
            
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= 12345
        result = tempProducto.modify_Producto(newIdProducto, newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el productoa modificar es None. 
    def testmodify_ProductoDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 1
        newDescripProducto= None
        result = tempProducto.modify_Producto( newIdProducto, newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es Entero y id string . 
    def testmodify_ProductoIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 'malo'
        newDescripProducto= 1212
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es Float y id string . 
    def testmodify_ProductoIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 'malo'
        newDescripProducto= 1212.23
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id string . 
    def testmodify_ProductoIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 'malo'
        newDescripProducto= None
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 500 y id string . 
    def testmodify_ProductoIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 'malo'
        newDescripProducto= 'y'*500
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 501 y id string . 
    def testmodify_ProductoIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 'malo'
        newDescripProducto= 'y'*501
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño Entero y id float . 
    def testmodify_ProductoIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 23.23
        newDescripProducto= 23
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño Float y id float . 
    def testmodify_ProductoIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 23.23
        newDescripProducto= 23.23
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id float . 
    def testmodify_ProductoIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 23.23
        newDescripProducto= None
        result = tempProducto.modify_Producto( newIdProducto, newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el productoa modificar es tamaño 500 y id float . 
    def testmodify_ProductoIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 23.23
        newDescripProducto= 'y'*500
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 501 y id float . 
    def testmodify_ProductoIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 23.23
        newDescripProducto= 'y'*501
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es entero y id None . 
    def testmodify_ProductoIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= None
        newDescripProducto= 23
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es float y id None . 
    def testmodify_ProductoIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= None
        newDescripProducto= 23.23
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id None . 
    def testmodify_ProductoIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= None
        newDescripProducto= None
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 500 y id None . 
    def testmodify_ProductoIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= None
        newDescripProducto= 'y'*500
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 501 y id None . 
    def testmodify_ProductoIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
     
        newIdProducto= 1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= None
        newDescripProducto= 'y'*501
        result = tempProducto.modify_Producto( newIdProducto, newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el productoa modificar es Entero y id MAX . 
    def testmodify_ProductoIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        newIdProducto= 2**31 -1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 2**31 -1
        newDescripProducto= 43
        result = tempProducto.modify_Producto( newIdProducto, newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es float y id MAX . 
    def testmodify_ProductoIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto= 2**31 -1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila( newIdProducto,newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 2**31 -1
        newDescripProducto= 43.323
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es None y id MAX . 
    def testmodify_ProductoIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
      
        newIdProducto= 2**31 -1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila(newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 2**31 -1
        newDescripProducto= None
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el productoa modificar es tamaño 500 y id MAX . 
    def testmodify_ProductoIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
      
        newIdProducto= 2**31 -1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila(newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 2**31 -1
        newDescripProducto= 'y'*500
        result = tempProducto.modify_Producto(newIdProducto, newDescripProducto)
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el producto a modificar es tamaño 501 y id MAX . 
    def testmodify_ProductoIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
      
        newIdProducto= 2**31 -1
        newDescripProducto= 'Esto es una prueba.'
        newProducto= model.Pila(newIdProducto, newDescripProducto) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
          
        tempProducto = clsProducto()
        newIdProducto= 2**31 -1
        newDescripProducto= 'y'*501
        result = tempProducto.modify_Producto( newIdProducto,newDescripProducto)
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #.-------------------------------------------------------------------.  