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
        model.db.session.query( model.Objetivo ).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Pila ).delete() 
    
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
    def testfind_idObjetivoExist(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()

    # Buscar el id de un objetivo con base de datos vacia
    def testfind_idObjetivoNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1000
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un objetivo con base de datos un elemento y busqueda no exitosa
        
    def testfind_idObjetivoNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdObjetivo = 2
        newDescripObjetivo = 'Esto es una prueba'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un objetivo con base de datos de varios elemento y busqueda no exitosa   
    def testfind_idObjetivoNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdObjetivo = indice
            newDescripObjetivo = 'Descripcion ' + str(indice)
            newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
            model.db.session.add(newObjetivo)
            model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 5
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un objetivo con base de datos de varios elemento y busqueda exitosa   
    def testfind_idObjetivoExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            newIdObjetivo = indice
            newDescripObjetivo = 'Descripcion ' + str(indice)
            newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
            model.db.session.add(newObjetivo)
            model.db.session.commit()   
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 3
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertIsNotNone( query[0] )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del objetivo a buscar es un string.
    def testfind_idObjetivoString(self):
        self.vaciarBaseDeDatos()
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = '1'
        query = tempObjetivo.find_idObjetivo(newIdProducto, idObjetivo )
        self.assertEqual(query,[])
        
        self.vaciarBaseDeDatos()
        
    # El id del objetivo a buscar es de tipo float.
    def testfind_idObjetivoFloat(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1.01
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del objetivo a buscar es nulo.
    def testfind_idObjetivoNone(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()

    #  El id del objetivo a buscar es negativo.
    def testfind_idObjetivoNegative(self):
        self.vaciarBaseDeDatos()

        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = -3
        query = tempObjetivo.find_idObjetivo( newIdProducto,idObjetivo )
        self.assertEqual(query,[])  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un objetivo con un elemento en la base de datos vacia.
    def testinsert_ObjetivoBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdObjetivo = 3
        newDescripObjetivo = 'Esto es una prueba'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
        

        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un objetivo con la base de datos vacia.
    def testinsert_ObjetivoBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        

        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un objetivo con varios elementos en la base de datos.
    def testinsert_ObjetivoBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(5,10,1):
            newIdObjetivo = indice
            newDescripObjetivo = 'Descripcion ' + str(indice)
            newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
            model.db.session.add(newObjetivo)
            model.db.session.commit()   
            
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'Objetivo 2.0'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un objetivo cuyo tama�o es igual a 1.
    def testinsert_ObjetivoDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = '1'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un objetivo cuyo tama�o es igual a 500.
    def testinsert_ObjetivoDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un Objetivo cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_ObjetivoDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = ''
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuyo tama�o es de 501.
    def testinsert_ObjetivoDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una Objetivo cuya descripcion es un numero.
    def testinsert_ObjetivoDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 501
        result = tempObjetivo.insert_Objetivo(newIdProducto, newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya descripcion dada es None.
    def testinsert_ObjetivoDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya descripcion dada es Float.
    def testinsert_ObjetivoDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 0.54
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo cuya escala dada es Float.
    def testinsert_ObjetivoEscalaFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = "descripcion"
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0.3)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya escala dada es None
    def testinsert_ObjetivoEscalaNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = "descripcion"
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,None)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya escala dada es String
    def testinsert_ObjetivoEscalaString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = "descripcion"
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,"None")
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo cuya escala dada es negativa
    def testinsert_ObjetivoEscalaNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = "descripcion"
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,-3)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo cuya escala dada es 3
    def testinsert_ObjetivoEscalaIsTres(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = "descripcion"
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,3)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #Se insertara un objetivo con id string
    def testinsert_ObjetivoIdString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'ola k ase'
        result = tempObjetivo.insert_Objetivo( 'error',newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un objetivo con id Float
    def testinsert_ObjetivoIdFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.insert_Objetivo(1.32,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                

    # Se insertara un Objetivo con id float.
    def testinsert_ObjetivoIdNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'None.. uff caiste'
        result = tempObjetivo.insert_Objetivo( None,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id maximo.
    def testinsert_ObjetivoIdGrant(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'None.. uff caiste'
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo.
    def testinsert_ObjetivoIdNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'None.. uff caiste'
        result = tempObjetivo.insert_Objetivo( -3,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion entero.
    def testinsert_ObjetivoIdStringDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 123
        result = tempObjetivo.insert_Objetivo( 'newIdProducto',newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion float.
    def testinsert_ObjetivoIdStringDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 23.23
        result = tempObjetivo.insert_Objetivo( 'newIdProducto',newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion None.
    def testinsert_ObjetivoIdStringDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( 'newIdProducto',newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id string y descripcion tamaño 500.
    def testinsert_ObjetivoIdStringDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.insert_Objetivo( 'newIdProducto',newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id string y descripcion tamaño 501.
    def testinsert_ObjetivoIdStringDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.insert_Objetivo( 'newIdProducto',newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion entero.
    def testinsert_ObjetivoIdFloatDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 32
        result = tempObjetivo.insert_Objetivo( 43.32,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion float.
    def testinsert_ObjetivoIdFloatDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 32.323
        result = tempObjetivo.insert_Objetivo( 43.32,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion None.
    def testinsert_ObjetivoIdFloatDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( 43.32,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion tamaño 500.
    def testinsert_ObjetivoIdFloatDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.insert_Objetivo( 43.32,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id float y descripcion tamaño 501.
    def testinsert_ObjetivoIdFloatDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.insert_Objetivo( 43.32,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion entero.
    def testinsert_ObjetivoIdNoneDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 34
        result = tempObjetivo.insert_Objetivo( None,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion float.
    def testinsert_ObjetivoIdNoneDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 34.23
        result = tempObjetivo.insert_Objetivo( None,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion None.
    def testinsert_ObjetivoIdNoneDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( None,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id None y descripcion 500.
    def testinsert_ObjetivoIdNoneDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.insert_Objetivo( None,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id None y descripcion 501.
    def testinsert_ObjetivoIdNoneDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.insert_Objetivo( None,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion entero.
    def testinsert_ObjetivoIdGrantDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 34
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id Grande y descripcion float.
    def testinsert_ObjetivoIdGrantDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 34.32
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion None.
    def testinsert_ObjetivoIdGrantDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion 500.
    def testinsert_ObjetivoIdGrantDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id Grande y descripcion 501.
    def testinsert_ObjetivoIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.insert_Objetivo( newIdProducto,newDescripObjetivo ,0)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
 
     # Se insertara un Objetivo con id Negativo y descripcion entero.
    def testinsert_ObjetivoIdNegativeDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 34
        result = tempObjetivo.insert_Objetivo( -3,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un Objetivo con id negativo y descripcion float.
    def testinsert_ObjetivoIdNegativeDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 34.32
        result = tempObjetivo.insert_Objetivo( -3,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo y descripcion None.
    def testinsert_ObjetivoIdNegativeDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = None
        result = tempObjetivo.insert_Objetivo( -3,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo y descripcion 500.
    def testinsert_ObjetivoIdNegativeDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.insert_Objetivo( -3,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un Objetivo con id negativo y descripcion 501.
    def testinsert_ObjetivoIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 2**31 - 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.insert_Objetivo( -3 ,newDescripObjetivo,0 )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del objetivo a modificar existe en la base de datos de un elemento.
    def testmodify_ObjetivoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoX'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testmodify_ObjetivoNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 20
        newDescripObjetivo = 'Esto sigue siendo una prueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del objetivo a modificar existe en la base de datos de varios objetivos 
    def testmodify_ObjetivoIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(1,10,1):
            newIdObjetivo = indice
            newDescripObjetivo = 'Descripcion ' + str(indice)
            newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
            model.db.session.add(newObjetivo)
            model.db.session.commit()   
            
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'esto sigue siendo una prueva V2'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del objetivo a modificar no existe en la base de datos de varios objetivos 
    def testmodify_ObjetivoIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        for indice in range(2,10,1):
            newIdObjetivo = indice
            newDescripObjetivo = 'Descripcion ' + str(indice)
            newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 ) 
            model.db.session.add(newObjetivo)
            model.db.session.commit()   
            
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'esto sigue siendo una prueva V2'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del objetivo a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_ObjetivoIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'l'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del objetivo a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_ObjetivoIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit() 
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.modify_Objetivo(newIdProducto, idObjetivo, newDescripObjetivo,0 )
        model.db.session.query(model.Objetivo).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del objetivo a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_ObjetivoIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdObjetivo = 1
        newDescripObjetivo = 'z'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'z'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del objetivo a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_ObjetivoIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
        
        newIdObjetivo = 1
        newDescripObjetivo = 'x'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del objetivo a modificar es un string.
    def testmodify_ObjetivoIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
            
        tempObjetivo = clsObjetivo()
        idObjetivo = '1'
        newDescripObjetivo = 'Axx'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testmodify_ObjetivoIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
           
        tempObjetivo = clsObjetivo()
        idObjetivo = -1
        newDescripObjetivo = 'Objetivo de prueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del objetivo a modificar es un float.
    def testmodify_ObjetivoIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 1.0
        newDescripObjetivo = 'Objetivo de prueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del objetivo a modificar es None.         
    def testmodify_ObjetivoIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La escala dada del objetivo a modificar es None.         
    def testmodify_ObjetivoEscalaNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,None )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La escala dada del objetivo a modificar es String         
    def testmodify_ObjetivoEscalaString(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,"None" )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La escala dada del objetivo a modificar es float        
    def testmodify_ObjetivoEscalaFloat(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0.3 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La escala dada del objetivo a modificar es negativa       
    def testmodify_ObjetivoEscalaNegative(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,-3 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La escala dada del objetivo a modificar es tres      
    def testmodify_ObjetivoEscalaIsTres(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'ObjetivoPrueba'
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,3 )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_ObjetivoDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()   
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()
             
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = ''
        result = tempObjetivo.modify_Objetivo(newIdProducto, idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es de longitud 501.    
    def testmodify_ObjetivoDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
           
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()
           
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 'r'*501
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el objetivo a modificar es un numero.
    def testmodify_ObjetivoDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit() 
            
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = 12345
        result = tempObjetivo.modify_Objetivo(newIdProducto, idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el objetivo a modificar es None. 
    def testmodify_ObjetivoDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 1
        newDescripObjetivo = None
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es Entero y id string . 
    def testmodify_ObjetivoIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        newDescripObjetivo = 1212
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es Float y id string . 
    def testmodify_ObjetivoIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        newDescripObjetivo = 1212.23
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id string . 
    def testmodify_ObjetivoIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        newDescripObjetivo = None
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id string . 
    def testmodify_ObjetivoIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id string . 
    def testmodify_ObjetivoIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 'malo'
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño Entero y id float . 
    def testmodify_ObjetivoIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        newDescripObjetivo = 23
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño Float y id float . 
    def testmodify_ObjetivoIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        newDescripObjetivo = 23.23
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id float . 
    def testmodify_ObjetivoIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        newDescripObjetivo = None
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id float . 
    def testmodify_ObjetivoIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id float . 
    def testmodify_ObjetivoIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 23.23
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es entero y id None . 
    def testmodify_ObjetivoIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = 23
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es float y id None . 
    def testmodify_ObjetivoIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = 23.23
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id None . 
    def testmodify_ObjetivoIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = None
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id None . 
    def testmodify_ObjetivoIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id None . 
    def testmodify_ObjetivoIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = None
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el objetivo a modificar es Entero y id MAX . 
    def testmodify_ObjetivoIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 2**31 -1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        newDescripObjetivo = 43
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es float y id MAX . 
    def testmodify_ObjetivoIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 2**31 -1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        newDescripObjetivo = 43.323
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es None y id MAX . 
    def testmodify_ObjetivoIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 2**31 -1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        newDescripObjetivo = None
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 500 y id MAX . 
    def testmodify_ObjetivoIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 2**31 -1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        newDescripObjetivo = 'y'*500
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el objetivo a modificar es tamaño 501 y id MAX . 
    def testmodify_ObjetivoIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto=model.Pila(newIdProducto,"producto",newDescripProducto,1) 
        model.db.session.add(newProducto)
        model.db.session.commit()  
        
        newIdObjetivo = 2**31 -1
        newDescripObjetivo = 'Esto es una prueba.'
        newObjetivo = model.Objetivo( newIdProducto,newIdObjetivo, newDescripObjetivo,0 )  
        model.db.session.add(newObjetivo)
        model.db.session.commit()   
          
        tempObjetivo = clsObjetivo()
        idObjetivo = 2**31 -1
        newDescripObjetivo = 'y'*501
        result = tempObjetivo.modify_Objetivo( newIdProducto,idObjetivo, newDescripObjetivo,0 )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    #.-------------------------------------------------------------------.