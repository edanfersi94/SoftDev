# -*- coding: utf-8 -*-

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
        model.db.session.query( model.Historias ).delete()
        model.db.session.query( model.Acciones ).delete()
        model.db.session.query( model.Categorias ).delete() 
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
        nuevaHistoria = model.Historias( idHistoria, codigo, idProducto, tipo, idAccion , idSuper, idEscala ) 
        model.db.session.add(nuevaHistoria)
        model.db.session.commit()

    def crearCategoria(self, idCategoria, nombreCategoria, pesoCategoria):
    	nuevaCategoria = model.Categorias( idCategoria, nombreCategoria, pesoCategoria )
    	model.db.session.add(nuevaCategoria)
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
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1,'nombre',1)


        nuevoIdTarea = 8
        nuevaDescTarea = 'caso de prueba'
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, 1)

        tempTarea = clsTarea()
        nuevaDescTarea = 'tarea 2.0'
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar una tarea con la base de datos vacia.
    def testinsert_TareaBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = 'tarea 2.0'
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar una tarea con varios elementos en la base de datos.
    def testinsert_TareaBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoPesoTarea = 1
        for indice in range(5,10,1):
            nuevoIdTarea = indice
            nuevaDescTarea  = 'Esto es una prueba ' + str(indice)
            nuevaTarea = model.Tareas( nuevoIdTarea, 1 , nuevaDescTarea, 1 , nuevoPesoTarea ) 
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        nuevaDescTarea = 'tarea 2.0'
        resultado = tempTarea.insertar(1, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara una tarea cuyo tamanio es igual a 1.
    def testinsert_TareaDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = '1'
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertTrue(resultado)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara una tarea cuyo tamanio es igual a 500.
    def testinsert_TareaDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertTrue(resultado)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara una tarea cuyo tamanio es 0 (Cadena vacia).
    def testinsert_TareaDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = ''
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuyo tamanio es de 501.
    def testinsert_TareaDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion es un numero.
    def testinsert_TareaDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = 501
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion es None.
    def testinsert_TareaDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = None
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion dada es Float.
    def testinsert_TareaDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        nuevaDescTarea = 0.54
        nuevoPesoTarea = 1
        resultado = tempTarea.insertar(1,nuevaDescTarea,1,nuevoPesoTarea)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id de la tarea a modificar existe en la base de datos de un elemento.
    def testmodify_TareaExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)

        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdTarea = 8
        nuevaDescTarea = 'caso de prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)
        model.db.session.add(nuevaTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 8
        nuevaDescTarea = 'accionX'
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id de la tarea a modificar no existe en la base de datos vacia.
    def testmodify_TareaNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        idTarea = 20
        nuevaDescTarea = 'Esto sigue siendo una prueba'
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id de la tarea a modificar existe en la base de datos de varias tareas 
    def testmodify_TareaIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoPesoTarea = 1
        for indice in range(1,10,1):
            nuevoIdTarea = indice
            nuevaDescTarea = 'Descripcion ' + str(indice)
            nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'esto sigue siendo una prueva V2'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id de la tarea a modificar no existe en la base de datos de varias tareas 
    def testmodify_TareaIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoPesoTarea = 1
        for indice in range(2,10,1):
            nuevoIdTarea = indice
            nuevaDescTarea = 'Descripcion ' + str(indice)
            nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'esto sigue siendo una prueva V2'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id de la tarea a modificar existe en la base de datos. La nueva 
    #          descripcion es de largo 1.
    def testmodify_TareaIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'l'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id de la tarea a modificar existe en la base de datos. La nueva 
    #          descripcion es de largo 500.
    def testmodify_TareaIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)
        model.db.session.add(nuevaTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
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
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'z'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'z'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id de la tarea a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripcion es de longitud igual a 500.
    def testmodify_TareaIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'x'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )

    # El id dado de la tarea a modificar es un string.
    def testmodify_TareaIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'Axx'
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado de la tarea a modificar es un numero negativo.    
    def testmodify_TareaIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'accion de prueba'
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado de la tarea a modificar es un float.
    def testmodify_TareaIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        idTarea = 1.0
        nuevaDescTarea = 'accion de prueba'
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado de la tarea a modificar es None.         
    def testmodify_TareaIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)

        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'accionPrueba'
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripcion para la accion a modificar es un string vacio.
    def testmodify_TareaDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)    
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = ''
        nuevoPesoTarea = 1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es de longitud 501.    
    def testmodify_TareaDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
           
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'r'*501
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripcion para la tarea a modificar es un numero.
    def testmodify_TareaDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 12345
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripcion para la tarea a modificar es None. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # El nuevo peso para la tarea a modificar es negativo. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'accionPrueba'
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # El nuevo peso para la tarea a modificar es float. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'accionPrueba'
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # El nuevo peso para la tarea a modificar es string. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'accionPrueba'
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # El nuevo peso para la tarea a modificar es None. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        nuevaDescTarea = 'accionPrueba'
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
    # La nueva descripcion para la tarea a modificar es Entero y id string . 
    def testmodify_TareaIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 1212
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es Float y id string . 
    def testmodify_TareaIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 1212.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id string . 
    def testmodify_TareaIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 500 y id string . 
    def testmodify_TareaIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id string . 
    def testmodify_TareaIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea= clsTarea()
        idTarea = 'malo'
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio Entero y id float . 
    def testmodify_TareaIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea= 23.23
        nuevaDescTarea = 23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio Float y id float . 
    def testmodify_TareaIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = 23.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id float . 
    def testmodify_TareaIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripcion para la tarea a modificar es tamanio 500 y id float . 
    def testmodify_TareaIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id float . 
    def testmodify_TareaIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es entero y id None . 
    def testmodify_TareaIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es float y id None . 
    def testmodify_TareaIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)   
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 23.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id None . 
    def testmodify_TareaIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 500 y id None . 
    def testmodify_TareaIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id None . 
    def testmodify_TareaIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripcion para la tarea a modificar es Entero y id MAX . 
    def testmodify_TareaIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 43
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es float y id MAX . 
    def testmodify_TareaIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 43.323
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es None y id MAX . 
    def testmodify_TareaIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1) 
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 500 y id MAX . 
    def testmodify_TareaIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 'y'*500
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripcion para la tarea a modificar es tamanio 501 y id MAX . 
    def testmodify_TareaIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 2**31 -1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        nuevaDescTarea = 'y'*501
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 



#--------#





	# id string, descripcion de tamaño 501, peso string
    def testmodify_TareaIdIsStringDescIsLen501PesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)   
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id string, descripcion es un numero, peso string
    def testmodify_TareaIdIsStringDescIsIntPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion vacia, peso string
    def testmodify_TareaIdIsStringDescIsEmptyPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = ''
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion float, peso string
    def testmodify_TareaIdIsStringDescIsFloatPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1.23
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion None, peso string
    def testmodify_TareaIdIsStringDescIsNonePesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = None
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


# id string, descripcion de tamaño 501, peso negativo
    def testmodify_TareaIdIsStringDescIsLen501PesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id string, descripcion es un numero, peso negativo
    def testmodify_TareaIdIsStringDescIsIntPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion vacia, peso negativo
    def testmodify_TareaIdIsStringDescIsEmptyPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = ''
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion float, peso negativo
    def testmodify_TareaIdIsStringDescIsFloatPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1.23
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion None, peso negativo
    def testmodify_TareaIdIsStringDescIsNonePesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = None
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion de tamaño 501, peso float
    def testmodify_TareaIdIsStringDescIsLen501PesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id string, descripcion es un numero, peso float
    def testmodify_TareaIdIsStringDescIsIntPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion vacia, peso float
    def testmodify_TareaIdIsStringDescIsEmptyPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = ''
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion float, peso float
    def testmodify_TareaIdIsStringDescIsFloatPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion None, peso float
    def testmodify_TareaIdIsStringDescIsNonePesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = None
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion de tamaño 501, peso None
    def testmodify_TareaIdIsStringDescIsLen501PesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id string, descripcion es un numero, peso None
    def testmodify_TareaIdIsStringDescIsIntPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion vacia, peso None
    def testmodify_TareaIdIsStringDescIsEmptyPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = ''
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion float, peso None
    def testmodify_TareaIdIsStringDescIsFloatPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1.23
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion None, peso None
    def testmodify_TareaIdIsStringDescIsNonePesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = None
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion de tamaño 501, peso excedido
    def testmodify_TareaIdIsStringDescIsLen501PesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id string, descripcion es un numero, peso excedido
    def testmodify_TareaIdIsStringDescIsIntPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion vacia, peso excedido
    def testmodify_TareaIdIsStringDescIsEmptyPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = ''
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id string, descripcion float, peso excedido
    def testmodify_TareaIdIsStringDescIsFloatPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id string, descripcion None, peso excedido
    def testmodify_TareaIdIsStringDescIsNonePesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = '1'
        nuevaDescTarea = None
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion de tamaño 501, peso string
    def testmodify_TareaIdIsNegativeDescIsLen501PesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id negativo, descripcion es un numero, peso string
    def testmodify_TareaIdIsNegativeDescIsIntPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion vacia, peso string
    def testmodify_TareaIdIsNegativeDescIsEmptyPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = ''
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion float, peso string
    def testmodify_TareaIdIsNegativeDescIsFloatPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1.23
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion None, peso string
    def testmodify_TareaIdIsNegativeDescIsNonePesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = None
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


# id negativo, descripcion de tamaño 501, peso negativo
    def testmodify_TareaIdIsNegativeDescIsLen501PesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id negativo, descripcion es un numero, peso negativo
    def testmodify_TareaIdIsNegativeDescIsIntPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion vacia, peso negativo
    def testmodify_TareaIdIsNegativeDescIsEmptyPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = ''
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion float, peso negativo
    def testmodify_TareaIdIsNegativeDescIsFloatPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1.23
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion None, peso negativo
    def testmodify_TareaIdIsNegativeDescIsNonePesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = None
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion de tamaño 501, peso float
    def testmodify_TareaIdIsNegativeDescIsLen501PesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id negativo, descripcion es un numero, peso float
    def testmodify_TareaIdIsNegativeDescIsIntPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion vacia, peso float
    def testmodify_TareaIdIsNegativeDescIsEmptyPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = ''
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion float, peso float
    def testmodify_TareaIdIsNegativeDescIsFloatPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion None, peso float
    def testmodify_TareaIdIsNegativeDescIsNonePesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = None
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion de tamaño 501, peso None
    def testmodify_TareaIdIsNegativeDescIsLen501PesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id negativo, descripcion es un numero, peso None
    def testmodify_TareaIdIsNegativeDescIsIntPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion vacia, peso None
    def testmodify_TareaIdIsNegativeDescIsEmptyPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = ''
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion float, peso None
    def testmodify_TareaIdIsNegativeDescIsFloatPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1.23
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion None, peso None
    def testmodify_TareaIdIsNegativeDescIsNonePesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = None
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion de tamaño 501, peso excedido
    def testmodify_TareaIdIsNegativeDescIsLen501PesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id negativo, descripcion es un numero, peso excedido
    def testmodify_TareaIdIsNegativeDescIsIntPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion vacia, peso excedido
    def testmodify_TareaIdIsNegativeDescIsEmptyPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = ''
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id negativo, descripcion float, peso excedido
    def testmodify_TareaIdIsNegativeDescIsFloatPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id negativo, descripcion None, peso excedido
    def testmodify_TareaIdIsNegativeDescIsNonePesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = -1
        nuevaDescTarea = None
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion de tamaño 501, peso string
    def testmodify_TareaIdIsFloatDescIsLen501PesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id float, descripcion es un numero, peso string
    def testmodify_TareaIdIsFloatDescIsIntPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion vacia, peso string
    def testmodify_TareaIdIsFloatDescIsEmptyPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = ''
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion float, peso string
    def testmodify_TareaIdIsFloatDescIsFloatPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1.23
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion None, peso string
    def testmodify_TareaIdIsFloatDescIsNonePesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = None
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


# id float, descripcion de tamaño 501, peso negativo
    def testmodify_TareaIdIsFloatDescIsLen501PesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id float, descripcion es un numero, peso negativo
    def testmodify_TareaIdIsFloatDescIsIntPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion vacia, peso negativo
    def testmodify_TareaIdIsFloatDescIsEmptyPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = ''
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion float, peso negativo
    def testmodify_TareaIdIsFloatDescIsFloatPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1.23
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion None, peso negativo
    def testmodify_TareaIdIsFloatDescIsNonePesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = None
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion de tamaño 501, peso float
    def testmodify_TareaIdIsFloatDescIsLen501PesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id float, descripcion es un numero, peso float
    def testmodify_TareaIdIsFloatDescIsIntPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion vacia, peso float
    def testmodify_TareaIdIsFloatDescIsEmptyPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = ''
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion float, peso float
    def testmodify_TareaIdIsFloatDescIsFloatPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion None, peso float
    def testmodify_TareaIdIsFloatDescIsNonePesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = None
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion de tamaño 501, peso None
    def testmodify_TareaIdIsFloatDescIsLen501PesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id float, descripcion es un numero, peso None
    def testmodify_TareaIdIsFloatDescIsIntPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion vacia, peso None
    def testmodify_TareaIdIsFloatDescIsEmptyPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = ''
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion float, peso None
    def testmodify_TareaIdIsFloatDescIsFloatPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1.23
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion None, peso None
    def testmodify_TareaIdIsFloatDescIsNonePesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = None
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion de tamaño 501, peso excedido
    def testmodify_TareaIdIsFloatDescIsLen501PesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id float, descripcion es un numero, peso excedido
    def testmodify_TareaIdIsFloatDescIsIntPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion vacia, peso excedido
    def testmodify_TareaIdIsFloatDescIsEmptyPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = ''
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id float, descripcion float, peso excedido
    def testmodify_TareaIdIsFloatDescIsFloatPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id float, descripcion None, peso excedido
    def testmodify_TareaIdIsFloatDescIsNonePesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1.23
        nuevaDescTarea = None
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion de tamaño 501, peso string
    def testmodify_TareaIdIsNoneDescIsLen501PesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id es None, descripcion es un numero, peso string
    def testmodify_TareaIdIsNoneDescIsIntPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion vacia, peso string
    def testmodify_TareaIdIsNoneDescIsEmptyPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = ''
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion float, peso string
    def testmodify_TareaIdIsNoneDescIsFloatPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1.23
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion None, peso string
    def testmodify_TareaIdIsNoneDescIsNonePesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


# id es None, descripcion de tamaño 501, peso negativo
    def testmodify_TareaIdIsNoneDescIsLen501PesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id es None, descripcion es un numero, peso negativo
    def testmodify_TareaIdIsNoneDescIsIntPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion vacia, peso negativo
    def testmodify_TareaIdIsNoneDescIsEmptyPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = ''
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion float, peso negativo
    def testmodify_TareaIdIsNoneDescIsFloatPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1.23
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion None, peso negativo
    def testmodify_TareaIdIsNoneDescIsNonePesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion de tamaño 501, peso float
    def testmodify_TareaIdIsNoneDescIsLen501PesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id es None, descripcion es un numero, peso float
    def testmodify_TareaIdIsNoneDescIsIntPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion vacia, peso float
    def testmodify_TareaIdIsNoneDescIsEmptyPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = ''
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion float, peso float
    def testmodify_TareaIdIsNoneDescIsFloatPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion None, peso float
    def testmodify_TareaIdIsNoneDescIsNonePesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion de tamaño 501, peso None
    def testmodify_TareaIdIsNoneDescIsLen501PesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id es None, descripcion es un numero, peso None
    def testmodify_TareaIdIsNoneDescIsIntPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion vacia, peso None
    def testmodify_TareaIdIsNoneDescIsEmptyPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = ''
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion float, peso None
    def testmodify_TareaIdIsNoneDescIsFloatPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1.23
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion None, peso None
    def testmodify_TareaIdIsNoneDescIsNonePesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion de tamaño 501, peso excedido
    def testmodify_TareaIdIsNoneDescIsLen501PesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id es None, descripcion es un numero, peso excedido
    def testmodify_TareaIdIsNoneDescIsIntPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion vacia, peso excedido
    def testmodify_TareaIdIsNoneDescIsEmptyPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = ''
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id es None, descripcion float, peso excedido
    def testmodify_TareaIdIsNoneDescIsFloatPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id es None, descripcion None, peso excedido
    def testmodify_TareaIdIsNoneDescIsNonePesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        nuevaDescTarea = None
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion de tamaño 501, peso string
    def testmodify_TareaIdIsOvervaluedDescIsLen501PesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id excedido, descripcion es un numero, peso string
    def testmodify_TareaIdIsOvervaluedDescIsIntPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion vacia, peso string
    def testmodify_TareaIdIsOvervaluedDescIsEmptyPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = ''
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion float, peso string
    def testmodify_TareaIdIsOvervaluedDescIsFloatPesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1.23
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion None, peso string
    def testmodify_TareaIdIsOvervaluedDescIsNonePesoIsString(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = None
        nuevoPesoTarea = '1'
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


# id excedido, descripcion de tamaño 501, peso negativo
    def testmodify_TareaIdIsOvervaluedDescIsLen501PesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id excedido, descripcion es un numero, peso negativo
    def testmodify_TareaIdIsOvervaluedDescIsIntPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion vacia, peso negativo
    def testmodify_TareaIdIsOvervaluedDescIsEmptyPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = ''
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion float, peso negativo
    def testmodify_TareaIdIsOvervaluedDescIsFloatPesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1.23
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion None, peso negativo
    def testmodify_TareaIdIsOvervaluedDescIsNonePesoIsNegative(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = None
        nuevoPesoTarea = -1
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion de tamaño 501, peso float
    def testmodify_TareaIdIsOvervaluedDescIsLen501PesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id excedido, descripcion es un numero, peso float
    def testmodify_TareaIdIsOvervaluedDescIsIntPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion vacia, peso float
    def testmodify_TareaIdIsOvervaluedDescIsEmptyPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = ''
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion float, peso float
    def testmodify_TareaIdIsOvervaluedDescIsFloatPesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion None, peso float
    def testmodify_TareaIdIsOvervaluedDescIsNonePesoIsFloat(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = None
        nuevoPesoTarea = 1.23
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion de tamaño 501, peso None
    def testmodify_TareaIdIsOvervaluedDescIsLen501PesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id excedido, descripcion es un numero, peso None
    def testmodify_TareaIdIsOvervaluedDescIsIntPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion vacia, peso None
    def testmodify_TareaIdIsOvervaluedDescIsEmptyPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = ''
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion float, peso None
    def testmodify_TareaIdIsOvervaluedDescIsFloatPesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1.23
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion None, peso None
    def testmodify_TareaIdIsOvervaluedDescIsNonePesoIsNone(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = None
        nuevoPesoTarea = None
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion de tamaño 501, peso excedido
    def testmodify_TareaIdIsOvervaluedDescIsLen501PesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 'y'*501
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # id excedido, descripcion es un numero, peso excedido
    def testmodify_TareaIdIsOvervaluedDescIsIntPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion vacia, peso excedido
    def testmodify_TareaIdIsOvervaluedDescIsEmptyPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = ''
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.


    # id excedido, descripcion float, peso excedido
    def testmodify_TareaIdIsOvervaluedDescIsFloatPesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = 1.23
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.

    # id excedido, descripcion None, peso excedido
    def testmodify_TareaIdIsOvervaluedDescIsNonePesoIsOvervalued(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)
        self.crearCategoria(1, 'nombre', 1)    
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba.'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas(nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea)  
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 2**31
        nuevaDescTarea = None
        nuevoPesoTarea = 2**31
        resultado = tempTarea.modificar(idTarea, nuevaDescTarea, 1, nuevoPesoTarea)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
	



#--------#
    




#.-------------------------------------------------------------------.
    # FUNCION ELIMINAR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Eliminar el id de una categoria que exista en la base de datos de un elemento. 
    def testEliminarIdCategoriaExist(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea ) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()   
        
        tempTarea = clsTarea()
        nuevoIdTarea = 1
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos()

    # Eliminar el id de una categoria con base de datos vacia
    def testEliminarIdCategoriaNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)
        
        tempTarea = clsTarea()
        nuevoIdTarea = 1000
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos()

        
    # Eliminar el id de una categoria con base de datos un elemento y busqueda no exitosa   
    def testEliminarIdCategoriaNotExistOneElementos(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea )
        model.db.session.add(nuevaTarea)
        model.db.session.commit()  
        
        tempTarea = clsTarea()
        nuevoIdTarea = 2
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos()
        
    # Eliminar el id de una categoria con base de datos de varios elemento y busqueda no exitosa   
    def testEliminarIdCategoriaNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)   
        
        for indice in range(1,4,1):
            nuevoIdTarea = indice
            nuevaDescTarea = 'Descripcion ' + str(indice)
            nuevoPesoTarea = 1
            nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea )  
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
        
        tempTarea = clsTarea()
        nuevoIdTarea = 5
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos()
          
    # Eliminar el id de una categoria con base de datos de varios elemento y busqueda exitosa   
    def testEliminarIdCategoriaExistVariosElementos(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1) 
        
        for indice in range(1,4,1):
            nuevoIdTarea = indice
            nuevaDescTarea = 'Descripcion ' + str(indice)
            nuevoPesoTarea = 1
            nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea )
            model.db.session.add(nuevaTarea)
            model.db.session.commit()   
        
        tempTarea = clsTarea()
        nuevoIdTarea = 3
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id de la categoria a Eliminar es un string.
    def testEliminarIdCategoriaString(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea ) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()

        tempTarea = clsTarea()
        nuevoIdTarea = '1'
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse(resultado)
        
        self.vaciarBaseDeDatos()
        
    # El id de la categoria a Eliminar es de tipo float.
    def testEliminarIdCategoriaFloat(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)
        
        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea )
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        nuevoIdTarea = 1.01
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse(resultado)  
        self.vaciarBaseDeDatos()

    #  El id de la categoria a Eliminar es nulo.
    def testEliminarIdCategoriaNone(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea ) 
        model.db.session.add(nuevaTarea)
        model.db.session.commit()

        tempTarea = clsTarea()
        nuevoIdTarea = None
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse(resultado)  
        self.vaciarBaseDeDatos()

    #  El id de la categoria a Eliminar es negativo.
    def testEliminarIdCategoriaNegative(self):
        self.vaciarBaseDeDatos()

        self.crearProducto(1, 'prueba', 'descripcion', 1)
        self.crearAccion(1, 1, 'esto es una prueba')
        self.crearHistoria(1, 'codigo', 1, 0, 1, 1, 1)  
        self.crearCategoria(1, 'nombre', 1)

        nuevoIdTarea = 1
        nuevaDescTarea = 'Esto es una prueba'
        nuevoPesoTarea = 1
        nuevaTarea = model.Tareas( nuevoIdTarea, 1, nuevaDescTarea, 1, nuevoPesoTarea )
        model.db.session.add(nuevaTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        nuevoIdTarea = -3
        resultado = tempTarea.eliminar( nuevoIdTarea )
        self.assertFalse(resultado)  
        self.vaciarBaseDeDatos()

    #.-------------------------------------------------------------------.
    #.-------------------------------------------------------------------.