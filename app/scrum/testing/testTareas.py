"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES: SoftDev
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcTarea.py"
    
"""

#--------------------------------------------------------------------------------------

# Librerias a utilizar
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

# PATH que permite utilizar al modulo "funcTarea.py"
sys.path.append('../')
from funcTarea import clsTarea

import unittest


class TestTareas(unittest.TestCase):
    
    # FUNCIONES AUXILIARES

    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Tareas ).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Productos ).delete() 
    
    def crearProducto(self, idProducto, nombreProducto, descProducto, escalaProducto):
        nuevoProducto = model.Productos( idProducto, nombreProducto, descProducto, escalaProducto )
        model.db.session.add(nuevoProducto)
        model.db.session.commit()

    def crearAccion(self, idProducto, idAccion, descAccion):
        nuevaAccion = model.Acciones( idProducto, idAccion , descAccion  ) 
        model.db.session.add(nuevaAccion)
        model.db.session.commit()

    def crearHistoria(self, idHistoria, codigo, idProducto, tipo, idAccion , idSuper, idEscala):
        newHistoria = model.Historias( idHistoria, codigo, idProducto, tipo, idAccion , idSuper, idEscala ) 
        model.db.session.add(newHistoria)
        model.db.session.commit()

    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsTarea.
    def testObjectExist(self):
        tempTarea = clsTarea()
        self.assertIsNotNone( tempTarea )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  

    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar una tarea con un elemento en la base de datos
    def testinsert_TareaBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)

        nuevoIdTarea = 8
        nuevaDescTarea = 'caso de prueba'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea )

        tempTarea = clsTarea()
        nuevaDescTarea = 'tarea 2.0'
        resultado = tempTarea.insertar( 1, nuevaDescTarea )
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar una tarea con la base de datos vacia.
    def testinsert_TareaBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        tempTarea = clsTarea()
        nuevaDescTarea = 'tarea 2.0'
        resultado = tempTarea.insertar( 1, nuevaDescTarea )
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar una tarea con varios elementos en la base de datos.
    def testinsert_TareaBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        for indice in range(5,10,1):
            nuevoIdTarea = indice
            nuevaDescTarea  = 'Esto es una prueba ' + str(indice)
            nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea ) 
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        nuevaDescTarea = 'tarea 2.0'
        resultado = tempTarea.insertar( 1, nuevaDescTarea )
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara una tarea cuyo tamanio es igual a 1.
    def testinsert_TareaDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        tempTarea = clsTarea()
        nuevaDescTarea = '1'
        resultado = tempTarea.insertar(1, nuevaDescTarea)
        self.assertTrue(resultado)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara una tarea cuyo tamanio es igual a 500.
    def testinsert_TareaDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        tempTarea = clsTarea()
        nuevaDescTarea ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        resultado = tempTarea.insertar(1, nuevaDescTarea)
        self.assertTrue(resultado)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara una tarea cuyo tamanio es 0 (Cadena vacia).
    def testinsert_TareaDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        tempTarea = clsTarea()
        nuevaDescTarea = ''
        resultado = tempTarea.insertar(1, nuevaDescTarea)
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuyo tamanio es de 501.
    def testinsert_TareaDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        tempTarea = clsTarea()
        nuevaDescTarea = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        resultado = tempTarea.insertar(1, nuevaDescTarea)
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion es un numero.
    def testinsert_TareaDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        tempTarea = clsTarea()
        newDescripTarea = 501
        resultado = tempTarea.insertar( 1, nuevaDescTarea)
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion dada es None.
    def testinsert_TareaDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        tempTarea = clsTarea()
        nuevaDescTarea = None
        resultado = tempTarea.insertar( 1, nuevaDescTarea)
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion dada es Float.
    def testinsert_TareaDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        tempTarea = clsTarea()
        nuevaDescTarea = 0.54
        resultado = tempTarea.insertar( 1, nuevaDescTarea)
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id de la tarea a modificar existe en la base de datos de un elemento.
    def testmodify_TareaExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 

        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdTarea = 8
        nuevaDescTarea = 'caso de prueba'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea )
        
        tempTarea = clsTarea()
        idTarea = 8
        nuevaDescTarea = 'accionX'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id de la tarea a modificar no existe en la base de datos vacia.
    def testmodify_TareaNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        tempTarea = clsTarea()
        idTarea = 20
        nuevaDescTarea = 'Esto sigue siendo una prueba'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id de la tarea a modificar existe en la base de datos de varias tareas 
    def testmodify_TareaIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        for indice in range(1,10,1):
            nuevoIdTarea = indice
            nuevaDescTarea = 'Descripcion ' + str(indice)
            nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea ) 
            model.db.session.add(nuevaTareaa)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'esto sigue siendo una prueva V2'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id de la tarea a modificar no existe en la base de datos de varias tareas 
    def testmodify_TareaIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        for indice in range(2,10,1):
            nuevoIdTarea = indice
            nuevaDescTarea = 'Descripcion ' + str(indice)
            nuevaTarea = model.Tareas( nuevoIdTarea , 1 , nuevaDescTarea ) 
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'esto sigue siendo una prueva V2'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id de la tarea a modificar existe en la base de datos. La nueva 
    #          descripcion es de largo 1.
    def testmodify_TareaIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'l'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id de la tarea a modificar existe en la base de datos. La nueva 
    #          descripcion es de largo 500.
    def testmodify_TareaIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 ,nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        model.db.session.query(model.Tareas).delete()  # Se limpia la base de datos.
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id de la tarea a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripcion es de longitud igual a 1.
    def testmodify_TareaIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'z'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'z'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id de la tarea a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripcion es de longitud igual a 500.
    def testmodify_TareaIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'x'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )

    # El id dado de la tarea a modificar es un string.
    def testmodify_TareaIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
            
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'Axx'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado de la tarea a modificar es un numero negativo.    
    def testmodify_TareaIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
           
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'accion de prueba'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado de la tarea a modificar es un float.
    def testmodify_TareaIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
          
        tempTarea = clsTarea()
        idTarea = 1.0
        nuevaDescTarea = 'accion de prueba'
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado de la tarea a modificar es None.         
    def testmodify_TareaIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'accionPrueba'
        resultado = tempTarea.modifIcar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripcion para la accion a modificar es un string vacio.
    def testmodify_TareaDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, nuevoIdHistoria, nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = ''
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es de longitud 501.    
    def testmodify_TareaDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
           
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'r'*501
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripcion para la tarea a modificar es un numero.
    def testmodify_TareaDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
            
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 12345
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripcion para la tarea a modificar es None. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = None
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es Entero y id string . 
    def testmodify_TareaIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 1212
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es Float y id string . 
    def testmodify_TareaIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 1212.23
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id string . 
    def testmodify_TareaIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = None
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 500 y id string . 
    def testmodify_TareaIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id string . 
    def testmodify_TareaIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea= clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio Entero y id float . 
    def testmodify_TareaIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea= 23.23
        nuevaDescTarea = 23
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio Float y id float . 
    def testmodify_TareaIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = 23.23
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id float . 
    def testmodify_TareaIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = None
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripcion para la tarea a modificar es tamanio 500 y id float . 
    def testmodify_TareaIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id float . 
    def testmodify_TareaIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es entero y id None . 
    def testmodify_TareaIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 23
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es float y id None . 
    def testmodify_TareaIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 23.23
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id None . 
    def testmodify_TareaIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 500 y id None . 
    def testmodify_TareaIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id None . 
    def testmodify_TareaIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripcion para la tarea a modificar es Entero y id MAX . 
    def testmodify_TareaIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 43
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es float y id MAX . 
    def testmodify_TareaIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 43.323
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id MAX . 
    def testmodify_TareaIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1) 
        
        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempAccion = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = None
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 500 y id MAX . 
    def testmodify_TareaIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id MAX . 
    def testmodify_TareaIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 'tipo', 1, 1, 1)  
        
        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar( idTarea, nuevaDescTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        



