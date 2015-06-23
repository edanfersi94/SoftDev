# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES: SoftDev
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcCategoria.py"
    
"""

#----------------------------------------------------------------------------

# Librerias a utilizar
import os
import sys

# PATH que permite utilizar el "model.py"
sys.path.append('../../../')
import model

sys.path.append('../')
from funcCategoria import clsCategoria



import unittest


class TestCategoria(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Categorias ).delete() 
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsCategoria.
    def testObjectExist(self):
        tempCategoria = clsCategoria()
        self.assertIsNotNone( tempCategoria )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar una categoria con un elemento en la base de datos.
    def testInsertarCategoriaBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'nombre prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un Categoria con la base de datos vacia.
    def testInsertarCategoriaBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertTrue(resultado[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un Categoria con varios elementos en la base de datos.
    def testInsertarCategoriaBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()

        
        for indice in range(5,10,1):
            nuevoIdCategoria = indice
            nuevoNombreCategoria = 'nombre ' + str(indice)
            nuevoPesoCategoria = 1
            nuevaCategoria = model.Categorias( nuevoIdCategoria,nuevoNombreCategoria, nuevoPesoCategoria) 
            model.db.session.add(nuevaCategoria)
            model.db.session.commit()   
            
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertTrue(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un Categoriacuyo tama�o es igual a 1.
    def testInsertarCategoriaDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria= '1'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertTrue(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un Categoria cuyo tama�o es igual a 500.
    def testInsertarCategoriaDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempCategoria = clsCategoria()
        nuevoNombreCategoria='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertTrue(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un Categoria cuyo tama�o es 0 (Cadena Vac�a).
    def testInsertarCategoriaDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria= ''
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una categoria cuyo nombre es de tamaño 501.
    def testInsertarCategoriaDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        tempCategoria = clsCategoria()
        nuevoNombreCategoria= 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una categoria cuyo nombre es un numero.
    def testInsertarCategoriaDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria= 501
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una categoria cuyo nombre es None.
    def testInsertarCategoriaDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        tempCategoria = clsCategoria()
        nuevoNombreCategoria= None
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una categoria cuyo nombre es Float.
    def testInsertarCategoriaDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria= 0.54
        nuevoPesoCategoria = 1
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar una categoria con peso string.
    def testInsertarCategoriaPesoString(self):
        self.vaciarBaseDeDatos()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = '1'
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Insertar una categoria con Peso None
    def testInsertarCategoriaPesoNone(self):
        self.vaciarBaseDeDatos()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = None
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar una categoria con Peso 0
    def testInsertarCategoriaPesoZero(self):
        self.vaciarBaseDeDatos()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = 0
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Insertar una categoria con Peso float
    def testInsertarCategoriaPesoFloat(self):
        self.vaciarBaseDeDatos()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = 1.29
        resultado = tempCategoria.insertar(nuevoNombreCategoria, nuevoPesoCategoria)
        self.assertFalse(resultado[0])
        
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id de la Categoria a modificar existe en la base de datos de un elemento.
    def testModificarCategoriaExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'nombre'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'otro nombre'
        nuevoPesoCategoria = 1
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id de la categoria a modificar existe en la base de datos de varios elementos 
    def testModificarCategoriaIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
       
        for indice in range(1,10,1):
            nuevoIdCategoria= indice
            nuevoNombreCategoria= 'nombre' + str(indice)
            nuevoPesoCategoria = 1
            nuevaCategoria= model.Categorias( nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria) 
            model.db.session.add(nuevaCategoria)
            model.db.session.commit()   
            
        tempCategoria = clsCategoria()
        nuevoIdCategoria = 3
        nuevoNombreCategoria = 'otro nombre'
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    

    
    #  El id de la categoria a modificar existe en la base de datos. El nuevo 
    #  nombre es de largo 1.
    def testModificarCategoriaIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevoPesoCategoria = 2
        nuevaCategoria= model.Categorias( nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria = 'l'
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue(resultado)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id de la categoria a modificar existe en la base de datos. El nuevo 
    #          nombre es de largo 500.
    def testModificarCategoriaIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevoPesoCategoria = 2
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'y'*500
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.resultado(model.Categorias).delete()  # Se limpia la base de datos.
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id de la categoria modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es de longitud igual a 1.
    def testModificarCategoriaIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'z'
        nuevoPesoCategoria = 2
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'a'
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id de la categoria a modificar existe en la base de datos y su valor es
    #          igual a 1. el nuevo nombre es de longitud igual a 500.
    def testModificarCategoriaIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
               
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue( resultado ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    
    # Peso de Categoria a modificar es un string.
    def testModificarCategoriaPesoString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
            
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = "2"
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # la Peso del Categoria a modificar es un None.
    def testModificarCategoriaPesoNone(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
            
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = None
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # la Peso del Categoria a modificar es un Float.
    def testModificarCategoriaPesoFloat(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
            
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = 3.32
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
    
    # la Peso del Categoria a modificar es un cero.
    def testModificarCategoriaPesoZero(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
            
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = 0
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
    # El id dado de la Categoria a modificar es un string.
    def testModificarCategoriaIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
            
        tempCategoria = clsCategoria()
        nuevoIdCategoria= '1'
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado de la categoria a modificar es un numero negativo.    
    def testModificarCategoriaIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
           
        tempCategoria = clsCategoria()
        nuevoIdCategoria= -1
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del Categoria a modificar es un float.
    def testModificarCategoriaIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1.0
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del Categoria a modificar es None.         
    def testModificarCategoriaIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria=' Descripcion Categoria.. '
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit() 
             
        tempCategoria = clsCategoria()
        nuevoIdCategoria= None
        nuevoNombreCategoria= ' Descripcion Categoria.. '
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El nuevo nombre para la categoria a modificar es un string vacio.
    def testModificarCategoriaDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba.'
        nuevaCategoria = model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
             
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= ''
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El nuevo nombre para la Categoria a modificar es de longitud 501.    
    def testModificarCategoriaDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
           
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
           
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'r'*501
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  El nuevo nombre para la Categoria a modificar es un numero.
    def testModificarCategoriaDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
            
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
        
        tempCategoria = clsCategoria()
        nuevoNombreCategoria= 12345
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El nuevo nombre para la Categoria a modificar es None. 
    def testModificarCategoriaDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 1
        nuevoNombreCategoria= None
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es Entero y id string . 
    def testModificarCategoriaIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 'malo'
        nuevoNombreCategoria= 1212
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es Float y id string . 
    def testModificarCategoriaIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 'malo'
        nuevoNombreCategoria= 1212.23
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es None y id string . 
    def testModificarCategoriaIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 'malo'
        nuevoNombreCategoria= None
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño 500 y id string . 
    def testModificarCategoriaIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 'malo'
        nuevoNombreCategoria= 'y'*500
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño 501 y id string . 
    def testModificarCategoriaIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 'malo'
        nuevoNombreCategoria= 'y'*501
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño Entero y id float . 
    def testModificarCategoriaIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 23.23
        nuevoNombreCategoria= 23
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño Float y id float . 
    def testModificarCategoriaIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 23.23
        nuevoNombreCategoria= 23.23
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es None y id float . 
    def testModificarCategoriaIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 23.23
        nuevoNombreCategoria= None
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # el nuevo nombre para la Categoria a modificar es tamaño 500 y id float . 
    def testModificarCategoriaIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 23.23
        nuevoNombreCategoria= 'y'*500
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño 501 y id float . 
    def testModificarCategoriaIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 23.23
        nuevoNombreCategoria= 'y'*501
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es entero y id None . 
    def testModificarCategoriaIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= None
        nuevoNombreCategoria= 23
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para el Categoriaa modificar es float y id None . 
    def testModificarCategoriaIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= None
        nuevoNombreCategoria= 23.23
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es None y id None . 
    def testModificarCategoriaIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= None
        nuevoNombreCategoria= None
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño 500 y id None . 
    def testModificarCategoriaIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= None
        nuevoNombreCategoria= 'y'*500
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es tamaño 501 y id None . 
    def testModificarCategoriaIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
     
        nuevoIdCategoria= 1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= None
        nuevoNombreCategoria= 'y'*501
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # el nuevo nombre para la Categoria a modificar es Entero y id MAX . 
    def testModificarCategoriaIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 43
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es float y id MAX . 
    def testModificarCategoriaIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 43.323
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # el nuevo nombre para la Categoria a modificar es None y id MAX . 
    def testModificarCategoriaIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
      
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= None
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El nuevo nombre para la Categoria a modificar es tamaño 500 y id MAX . 
    def testModificarCategoriaIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
      
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'y'*500
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El nuevo nombre para la Categoria a modificar es tamaño 501 y id MAX . 
    def testModificarCategoriaIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
      
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'Esto es una prueba.'
        nuevaCategoria= model.Categorias(nuevoIdCategoria,nuevoNombreCategoria,1)
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
          
        tempCategoria = clsCategoria()
        nuevoIdCategoria= 2**31 -1
        nuevoNombreCategoria= 'y'*501
        nuevoPesoCategoria = 2
        resultado = tempCategoria.modificar(nuevoIdCategoria,nuevoNombreCategoria,nuevoPesoCategoria)
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        


    #.-------------------------------------------------------------------.
    # FUNCION ELIMINAR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Eliminar el id de una categoria que exista en la base de datos de un elemento. 
    def testEliminarIdCategoriaExist(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria,nuevoPesoCategoria ) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()   
        
        tempCategoria = clsCategoria()
        nuevoIdCategoriagoria = 1
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos()

    # Eliminar el id de una categoria con base de datos vacia
    def testEliminarIdCategoriaNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria = 1000
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse( resultado )
        self.vaciarBaseDeDatos()

        
    # Eliminar el id de una categoria con base de datos un elemento y busqueda no exitosa
        
    def testEliminarIdCategoriaNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria, nuevoPesoCategoria ) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()  
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria = 2
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos()
        
    # Eliminar el id de una categoria con base de datos de varios elemento y busqueda no exitosa   
    def testEliminarIdCategoriaNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        
        for indice in range(1,4,1):
            nuevoIdCategoria = indice
            nuevoNombreCategoria = 'Descripcion ' + str(indice)
            nuevoPesoCategoria = 1
            nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria, nuevoPesoCategoria) 
            model.db.session.add(nuevaCategoria)
            model.db.session.commit()   
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria = 5
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse(resultado)
        self.vaciarBaseDeDatos()
          
    # Eliminar el id de una categoria con base de datos de varios elemento y busqueda exitosa   
    def testEliminarIdCategoriaExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        
        for indice in range(1,4,1):
            nuevoIdCategoria = indice
            nuevoNombreCategoria = 'Descripcion ' + str(indice)
            nuevoPesoCategoria = 1
            nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria , nuevoPesoCategoria)
            model.db.session.add(nuevaCategoria)
            model.db.session.commit()   
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria = 3
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertTrue( resultado )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id de la categoria a Eliminar es un string.
    def testEliminarIdCategoriaString(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria, nuevoPesoCategoria ) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()

        tempCategoria = clsCategoria()
        nuevoIdCategoria = '1'
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse(resultado)
        
        self.vaciarBaseDeDatos()
        
    # El id de la categoria a Eliminar es de tipo float.
    def testEliminarIdCategoriaFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria, nuevoPesoCategoria ) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria = 1.01
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse(resultado)  
        self.vaciarBaseDeDatos()

    #  El id de la categoria a Eliminar es nulo.
    def testEliminarIdCategoriaNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria, nuevoPesoCategoria ) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()

        tempCategoria = clsCategoria()
        nuevoIdCategoria = None
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse(resultado)  
        self.vaciarBaseDeDatos()

    #  El id de la categoria a Eliminar es negativo.
    def testEliminarIdCategoriaNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdCategoria = 1
        nuevoNombreCategoria = 'Esto es una prueba'
        nuevoPesoCategoria = 1
        nuevaCategoria = model.Categorias( nuevoIdCategoria, nuevoNombreCategoria, nuevoPesoCategoria ) 
        model.db.session.add(nuevaCategoria)
        model.db.session.commit()
        
        tempCategoria = clsCategoria()
        nuevoIdCategoria = -3
        resultado = tempCategoria.eliminar( nuevoIdCategoria )
        self.assertFalse(resultado)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.
    #.-------------------------------------------------------------------.