"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
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

        model.db.session.query( model.Acciones ).delete()

        model.db.session.query( model.Tareas ).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Historias ).delete()
        model.db.session.query( model.Productos ).delete() 
    
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
        
        newIdProducto = 1
        newDescripProducto =' Descripcion Producto.. '
        newProducto  = model.Productos(newIdProducto,'Producto',newDescripProducto,1 )
        model.db.session.add(newProducto )
        model.db.session.commit() 
        
        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()

        newIdTarea = 8
        newDescTarea = 'caso de prueba'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea )

        tempTarea = clsTarea()
        newDescTarea = 'tarea 2.0'
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar una tarea con la base de datos vacia.
    def testinsert_TareaBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        

        tempTarea = clsTarea()
        newDescTarea = 'tarea 2.0'
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar una tarea con varios elementos en la base de datos.
    def testinsert_TareaBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        for indice in range(5,10,1):
            newIdTarea = indice
            newDescTarea  = 'Esto es una prueba ' + str(indice)
            newTarea = model.Tareas( newIdTarea,newIdHistoria , newDescTarea ) 
            model.db.session.add(newTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        newDescTarea = 'tarea 2.0'
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara una tarea cuyo tama�o es igual a 1.
    def testinsert_TareaDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala ) 
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        newDescTarea = '1'
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertTrue(result)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara una tarea cuyo tama�o es igual a 500.
    def testinsert_TareaDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        newDescTarea ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertTrue(result)
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara una tarea cuyo tama�o es 0 (Cadena Vac�a).
    def testinsert_TareaDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        newDescTarea = ''
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuyo tama�o es de 501.
    def testinsert_TareaDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        newDescTarea = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempTarea.insertar( newIdHistoria, newDescTarea )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion es un numero.
    def testinsert_TareaDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        newDescripTarea = 501
        result = tempTarea.insertar( newIdHistoria, newDescTarea)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion dada es None.
    def testinsert_TareaDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        newDescTarea = None
        result = tempTarea.insertar( newIdHistoria, newDescTarea)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una tarea cuya descripcion dada es Float.
    def testinsert_TareaDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        newDescTarea = 0.54
        result = tempTarea.insertar( newIdHistoria, newDescTarea)
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id de la tarea a modificar existe en la base de datos de un elemento.
    def testmodify_TareaExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()

        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdTarea = 8
        newDescTarea = 'caso de prueba'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea )
        
        tempTarea = clsTarea()
        idTarea = 8
        newDescTarea = 'accionX'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id de la tarea a modificar no existe en la base de datos vacia.
    def testmodify_TareaNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 20
        newDescTarea = 'Esto sigue siendo una prueba'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id de la tarea a modificar existe en la base de datos de varias tareas 
    def testmodify_TareaIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        for indice in range(1,10,1):
            newIdTarea = indice
            newDescTarea = 'Descripcion ' + str(indice)
            newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea ) 
            model.db.session.add(newTareaa)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 'esto sigue siendo una prueva V2'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id de la tarea a modificar no existe en la base de datos de varias tareas 
    def testmodify_TareaIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        for indice in range(2,10,1):
            newIdTarea = indice
            newDescTarea = 'Descripcion ' + str(indice)
            newTarea = model.Tareas( newIdTarea , newIdHistoria , newDescTarea ) 
            model.db.session.add(newTarea)
            model.db.session.commit()   
            
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 'esto sigue siendo una prueva V2'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id de la tarea a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testmodify_TareaIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 'l'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id de la tarea a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testmodify_TareaIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit() 
        
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 'y'*500
        result = tempTarea.modificar( idTarea, newDescTarea )
        model.db.session.query(model.Tareas).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id de la tarea a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testmodify_TareaIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 1
        newDescTarea = 'z'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 'z'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id de la tarea a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testmodify_TareaIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 1
        newDescTarea = 'x'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )

    # El id dado de la tarea a modificar es un string.
    def testmodify_TareaIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
            
        tempTarea = clsTarea()
        idTarea = '1'
        newDescTarea = 'Axx'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado de la tarea a modificar es un numero negativo.    
    def testmodify_TareaIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
           
        tempTarea = clsTarea()
        idTarea = -1
        newDescTarea = 'accion de prueba'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado de la tarea a modificar es un float.
    def testmodify_TareaIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
          
        tempTarea = clsTarea()
        idTarea = 1.0
        newDescTarea = 'accion de prueba'
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado de la tarea a modificar es None.         
    def testmodify_TareaIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = None
        newDescTarea = 'accionPrueba'
        result = tempTarea.modifIcar( idTarea, newDescTarea )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testmodify_TareaDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()   
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()
             
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = ''
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es de longitud 501.    
    def testmodify_TareaDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 
           
        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()
           
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 'r'*501
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para la tarea a modificar es un numero.
    def testmodify_TareaDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
            
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()
        
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = 12345
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para la tarea a modificar es None. 
    def testmodify_TareaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 1
        newDescTarea = None
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es Entero y id string . 
    def testmodify_TareaIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        newDescTarea = 1212
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es Float y id string . 
    def testmodify_TareaIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        newDescTarea = 1212.23
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es None y id string . 
    def testmodify_TareaIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()  

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        newDescTarea = None
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 500 y id string . 
    def testmodify_TareaIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 'malo'
        newDescTarea = 'y'*500
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 501 y id string . 
    def testmodify_TareaIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea= clsTarea()
        idTarea = 'malo'
        newDescTarea = 'y'*501
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño Entero y id float . 
    def testmodify_TareaIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea= 23.23
        newDescTarea = 23
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño Float y id float . 
    def testmodify_TareaIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        newDescTarea = 23.23
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es None y id float . 
    def testmodify_TareaIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        newDescTarea = None
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para la tarea a modificar es tamaño 500 y id float . 
    def testmodify_TareaIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        newDescTarea = 'y'*500
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 501 y id float . 
    def testmodify_TareaIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 23.23
        newDescTarea = 'y'*501
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es entero y id None . 
    def testmodify_TareaIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        newDescTarea = 23
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es float y id None . 
    def testmodify_TareaIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        newDescTarea = 23.23
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es None y id None . 
    def testmodify_TareaIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea, newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        newDescTarea = None
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 500 y id None . 
    def testmodify_TareaIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        newDescTarea = 'y'*500
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 501 y id None . 
    def testmodify_TareaIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = None
        newDescTarea = 'y'*501
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para la tarea a modificar es Entero y id MAX . 
    def testmodify_TareaIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 2**31 -1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        newDescTarea = 43
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es float y id MAX . 
    def testmodify_TareaIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 2**31 -1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        newDescTarea = 43.323
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es None y id MAX . 
    def testmodify_TareaIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()  

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        newIdTarea = 2**31 -1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempAccion = clsTarea()
        idTarea = 2**31 -1
        newDescTarea = None
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 500 y id MAX . 
    def testmodify_TareaIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit() 

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit() 
        
        newIdTarea = 2**31 -1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        newDescTarea = 'y'*500
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para la tarea a modificar es tamaño 501 y id MAX . 
    def testmodify_TareaIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        newIdProducto = 1
        newDescripProducto=' Descripcion Producto.. '
        newProducto = model.Productos(newIdProducto,'Prodcuto',newDescripProducto,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        newIdAccion = 2
        newDescripAccion  = 'Esto es una prueba'
        newAccion = model.Acciones( newIdProducto,newIdAccion , newDescripAccion  ) 
        model.db.session.add(newAccion)
        model.db.session.commit()

        newIdHistoria = 2
        newTipo = 'caso'
        newCodigo = 'prueba'
        newIdSuper = 1
        newIdEscala = 1
        newDescripAccion  = 'Esto es una prueba'
        newHistoria = model.Historias( newIdHistoria,newCodigo,newIdProducto, newTipo, newIdAccion , newIdSuper, newIdEscala )
        model.db.session.add(newHistoria)
        model.db.session.commit()  
        
        newIdTarea = 2**31 -1
        newDescTarea = 'Esto es una prueba.'
        newTarea = model.Tareas( newIdTarea,newIdHistoria, newDescTarea) 
        model.db.session.add(newTarea)
        model.db.session.commit()   
          
        tempTarea = clsTarea()
        idTarea = 2**31 -1
        newDescTarea = 'y'*501
        result = tempTarea.modificar( idTarea, newDescTarea )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
