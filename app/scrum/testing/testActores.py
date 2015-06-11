"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcActor.py"
    
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

sys.path.append('../')
from funcActor import clsActor


import unittest


class TestActor(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query( model.Actores ).delete()  # Se limpia la base de datos.
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
    
    # Test 1: Se crea el objeto clsActor.
    def testObjectExist(self):
        self.vaciarBaseDeDatos()
        tempActor = clsActor()
        self.assertIsNotNone( tempActor )
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Buscar el id de un actor que exista en la base de datos de un elemento. 
    def testBuscarIdActorExist(self):
        self.vaciarBaseDeDatos()

        idProducto=1
        self.insertarProducto(idProducto)
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba'
        nuevoActor = model.Actores( idProducto,nuevoIdActor,'actor 1', nuevoDescripcionActor ) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 1
        query = tempActor.buscarId(idactor )
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()

    # Buscar el id de un actor con base de datos vacia
    def testBuscarIdActorNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = 1000
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()

        
    # Buscar el id de un actor con base de datos un elemento y busqueda no exitosa
        
    def testBuscarIdActorNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdActor = 2
        nuevoDescripcionActor = 'Esto es una prueba'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 1
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    # Buscar el id de un actor con base de datos de varios elemento y busqueda no exitosa   
    def testBuscarIdActorNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 5
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
          
    # Buscar el id de un actor con base de datos de varios elemento y busqueda exitosa   
    def testBuscarIdActorExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 3
        query = tempActor.buscarId( idactor )
        self.assertIsNotNone( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del actor a buscar es un string.
    def testBuscarIdActorString(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
 
        
        tempActor = clsActor()
        idactor = '1'
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)
        
        self.vaciarBaseDeDatos()
        
    # El id del actor a buscar es de tipo float.
    def testBuscarIdActorFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = 1.01
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del actor a buscar es nulo.
    def testBuscarIdActorNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempActor = clsActor()
        idactor = None
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()

    #  El id del actor a buscar es negativo.
    def testBuscarIdActorNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = -3
        query = tempActor.buscarId( idactor )
        self.assertEqual(query,None)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Insertar un actor con un elemento en la base de datos vacia.
    def testInsertarActorBaseDeDatosOneElem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 3
        nuevoDescripcionActor = 'Esto es una prueba'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
        

        tempActor = clsActor()
        nuevoDescripcionActor = 'accion 2.0'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.
        

    # Insertar un actor con la base de datos vacia.
    def testInsertarActorBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempActor = clsActor()
        nuevoDescripcionActor = 'accion 2.0'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Insertar un actor con varios elementos en la base de datos.
    def testInsertarActorBaseDeDatosVariosELem(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        for indice in range(5,10,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
            
        tempActor = clsActor()
        nuevoDescripcionActor = 'accion 2.0'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
                  
    ### CASOS VALIDOS( Casos Fronteras )
    #Se insertara un actor cuyo tama�o es igual a 1.
    def testInsertarActorDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = '1'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un actor cuyo tama�o es igual a 500.
    def testInsertarActorDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        tempActor = clsActor()
        nuevoDescripcionActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un actor cuyo tama�o es 0 (Cadena Vac�a).
    def testInsertarActorDescripLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = ''
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuyo tama�o es de 501.
    def testInsertarActorDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una actor cuya descripcion es un numero.
    def testInsertarActorDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 501
        result = tempActor.insertar(nuevoIdProducto,'Actor 2', nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuya descripcion dada es None.
    def testInsertarActorDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = None
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuya descripcion dada es Float.
    def testInsertarActorDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 0.54
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
   #Se insertara un actor cuyo tama�o es igual a 1.
    def testInsertarActorNameLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'sad1'
        result = tempActor.insertar( nuevoIdProducto,'2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un actor cuyo tama�o es igual a 500.
    def testInsertarActorNameLen50(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        tempActor = clsActor()
        nuevoDescripcionActor ='Loradipgula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insertar( nuevoIdProducto,'q'*50,nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    #  Se insertara un actor cuyo tama�o es 0 (Cadena Vac�a).
    def testInsertarActorNameLen0(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'Descripcion Actor'
        result = tempActor.insertar( nuevoIdProducto,'',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuyo tama�o es de 501.
    def testInsertarActorNameLen51(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'tibus et magnisntes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
        result = tempActor.insertar( nuevoIdProducto,'q'*51,nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara una actor cuya descripcion es un numero.
    def testInsertarActorNameInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = "Descripcion Actor"
        result = tempActor.insertar(nuevoIdProducto,2332, nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuya descripcion dada es None.
    def testInsertarActorNameNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = "Descripcion Actor"
        result = tempActor.insertar( nuevoIdProducto,None,nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor cuya descripcion dada es Float.
    def testInsertarActorNameFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = "Descripcion Actor"
        result = tempActor.insertar( nuevoIdProducto,3.2,nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #Se insertara un actor con id string
    def testInsertarActorIdString(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'ola k ase'
        result = tempActor.insertar( 'error','Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    #  Se insertara un actor con id Float
    def testInsertarActorIdFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.insertar(1.32,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                

    # Se insertara un actor con id float.
    def testInsertarActorIdNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'None.. uff caiste'
        result = tempActor.insertar( None,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id maximo.
    def testInsertarActorIdGrant(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'None.. uff caiste'
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo.
    def testInsertarActorIdNegative(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'None.. uff caiste'
        result = tempActor.insertar(-3,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion entero.
    def testInsertarActorIdStringDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 123
        result = tempActor.insertar( 'nuevoIdProducto','actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion float.
    def testInsertarActorIdStringDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 23.23
        result = tempActor.insertar( 'nuevoIdProducto','actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion None.
    def testInsertarActorIdStringDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = None
        result = tempActor.insertar( 'nuevoIdProducto','actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id string y descripcion tamaño 500.
    def testInsertarActorIdStringDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*500
        result = tempActor.insertar( 'nuevoIdProducto','actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id string y descripcion tamaño 501.
    def testInsertarActorIdStringDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*501
        result = tempActor.insertar( 'nuevoIdProducto','actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion entero.
    def testInsertarActorIdFloatDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 32
        result = tempActor.insertar( 43.32,'Actor 2 ',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion float.
    def testInsertarActorIdFloatDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 32.323
        result = tempActor.insertar( 43.32,'Actor 2 ',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion None.
    def testInsertarActorIdFloatDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = None
        result = tempActor.insertar( 43.32,'Actor 2 ',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion tamaño 500.
    def testInsertarActorIdFloatDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*500
        result = tempActor.insertar( 43.32,'Actor 2 ',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id float y descripcion tamaño 501.
    def testInsertarActorIdFloatDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*501
        result = tempActor.insertar( 43.32,'Actor 2 ',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion entero.
    def testInsertarActorIdNoneDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 34
        result = tempActor.insertar( None,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion float.
    def testInsertarActorIdNoneDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 34.23
        result = tempActor.insertar( None,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion None.
    def testInsertarActorIdNoneDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = None
        result = tempActor.insertar( None,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id None y descripcion 500.
    def testInsertarActorIdNoneDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*500
        result = tempActor.insertar( None,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id None y descripcion 501.
    def testInsertarActorIdNoneDescripLen501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*501
        result = tempActor.insertar( None,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion entero.
    def testInsertarActorIdGrantDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 34
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id Grande y descripcion float.
    def testInsertarActorIdGrantDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 34.32
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion None.
    def testInsertarActorIdGrantDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = None
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion 500.
    def testInsertarActorIdGrantDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*500
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id Grande y descripcion 501.
    def testInsertarActorIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*501
        result = tempActor.insertar( nuevoIdProducto,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
 
     # Se insertara un actor con id Negativo y descripcion entero.
    def testInsertarActorIdNegativeDescripInt(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 34
        result = tempActor.insertar( -3,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # Se insertara un actor con id negativo y descripcion float.
    def testInsertarActorIdNegativeDescripFloat(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 34.32
        result = tempActor.insertar( -3,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo y descripcion None.
    def testInsertarActorIdNegativeDescripNone(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = None
        result = tempActor.insertar( -3,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo y descripcion 500.
    def testInsertarActorIdNegativeDescrip500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*500
        result = tempActor.insertar(-3,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # Se insertara un actor con id negativo y descripcion 501.
    def testInsertarActorIdGrantDescrip501(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 2**31 - 1
        self.insertarProducto(nuevoIdProducto)
        model.db.session.commit() 
        
        tempActor = clsActor()
        nuevoDescripcionActor = 'y'*501
        result = tempActor.insertar( -3 ,'Actor 2',nuevoDescripcionActor )
        self.assertFalse(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.        
    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # El id del actor a modificar existe en la base de datos de un elemento.
    def testModificarActorExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit() 
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'accionX'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.      

    # El id del ojetivo a modificar no existe en la base de datos vacia.
    def testModificarActorNoExist(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = 20
        nuevoDescripcionActor = 'Esto sigue siendo una prueba'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # El id del actor a modificar existe en la base de datos de varios actors 
    def testModificarActorIdExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        for indice in range(1,10,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
            
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'esto sigue siendo una prueva V2'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  
    
    # El id del actor a modificar no existe en la base de datos de varios actors 
    def testModificarActorIdNotExistVariosELem(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        for indice in range(2,10,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
            
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'esto sigue siendo una prueva V2'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos.  

    
    #  El id del actor a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 1.
    def testModificarActorIdExistNewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit() 
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'l'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertTrue(result)
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    
    
    # El id del actor a modificar existe en la base de datos. La nueva 
    #          descripci�n es de largo 500.
    def testModificarActorIdExistNewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit() 
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'y'*500
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        model.db.session.query(model.Actores).delete()  # Se limpia la base de datos.
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

        
    
    ### CASOS VALIDOS( Casos Esquinas )
    #  El id del actor a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 1.
    def testModificarActorIdExistIqual1NewDescripLen1(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'z'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'z'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # El id del actor a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripci�n es de longitud igual a 500.
    def testModificarActorIdExistIqual1NewDescripLen500(self):
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'x'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor ='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertTrue( result ) 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    ### CASOS INVALIDOS( Casos Malicia )
    # El id dado del actor a modificar es un string.
    def testModificarActorIdString(self):    
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
            
        tempActor = clsActor()
        idactor = '1'
        nuevoDescripcionActor = 'Axx'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )  
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # El id dado del obetivo a modificar es un numero negativo.    
    def testModificarActorIdNegative(self):     
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
           
        tempActor = clsActor()
        idactor = -1
        nuevoDescripcionActor = 'accion de prueba'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
                
    # El id dado del actor a modificar es un float.
    def testModificarActorIdFloat(self):      
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
          
        tempActor = clsActor()
        idactor = 1.0
        nuevoDescripcionActor = 'accion de prueba'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # El id dado del actor a modificar es None.         
    def testModificarActorIdNone(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
             
        tempActor = clsActor()
        idactor = None
        nuevoDescripcionActor = 'accionPrueba'
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
    
    # La nueva descripci�n para la acci�n a modificar es un string vacio.
    def testModificarActorDescripIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
             
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = ''
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es de longitud 501.    
    def testModificarActorDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
           
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
           
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'r'*501
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva descripci�n para el actor a modificar es un numero.
    def testModificarActorDescripIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
            
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 12345
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva descripci�n para el actor a modificar es None. 
    def testModificarActorDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = None
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
  # La nueva name para la acci�n a modificar es un string vacio.
    def testModificarActorNameIsEmpty(self): 
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
             
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'descripcion actor'
        result = tempActor.modificar( idactor,'' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva name para el actor a modificar es de longitud 51.    
    def testModificarActorNameLen51(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
           
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
           
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'descripcion actor'
        result = tempActor.modificar( idactor,'q'*51 ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.    

    #  La nueva name para el actor a modificar es un numero.
    def testModificarActorNameIsNumber(self):   
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
            
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()
        
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'descripcion actor'
        result = tempActor.modificar( idactor,32 ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos.   
        
    # La nueva name para el actor a modificar es None. 
    def testModificarActorNameNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 1
        nuevoDescripcionActor = 'descripcion actor'
        result = tempActor.modificar( idactor,None ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        
    # La nueva descripci�n para el actor a modificar es Entero y id string . 
    def testModificarActorIdStringDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 'malo'
        nuevoDescripcionActor = 1212
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es Float y id string . 
    def testModificarActorIdStringDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 'malo'
        nuevoDescripcionActor = 1212.23
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id string . 
    def testModificarActorIdStringDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 'malo'
        nuevoDescripcionActor = None
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 500 y id string . 
    def testModificarActorIdStringDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 'malo'
        nuevoDescripcionActor = 'y'*500
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id string . 
    def testModificarActorIdStringDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 'malo'
        nuevoDescripcionActor = 'y'*501
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño Entero y id float . 
    def testModificarActorIdFloatDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 23.23
        nuevoDescripcionActor = 23
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño Float y id float . 
    def testModificarActorIdFloatDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 23.23
        nuevoDescripcionActor = 23.23
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id float . 
    def testModificarActorIdFloatDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 23.23
        nuevoDescripcionActor = None
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el actor a modificar es tamaño 500 y id float . 
    def testModificarActorIdFloatDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 23.23
        nuevoDescripcionActor = 'y'*500
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id float . 
    def testModificarActorIdFloatDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 23.23
        nuevoDescripcionActor = 'y'*501
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es entero y id None . 
    def testModificarActorIdNoneDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = None
        nuevoDescripcionActor = 23
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es float y id None . 
    def testModificarActorIdNoneDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = None
        nuevoDescripcionActor = 23.23
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id None . 
    def testModificarActorIdNoneDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = None
        nuevoDescripcionActor = None
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 500 y id None . 
    def testModificarActorIdNoneDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = None
        nuevoDescripcionActor = 'y'*500
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id None . 
    def testModificarActorIdNoneDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = None
        nuevoDescripcionActor = 'y'*501
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # La nueva descripci�n para el actor a modificar es Entero y id MAX . 
    def testModificarActorIdMaxDescripInt(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        nuevoIdActor = 2**31 -1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 2**31 -1
        nuevoDescripcionActor = 43
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es float y id MAX . 
    def testModificarActorIdMaxDescripFloat(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 2**31 -1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 2**31 -1
        nuevoDescripcionActor = 43.323
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es None y id MAX . 
    def testModificarActorIdMaxDescripNone(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto) 
        
        nuevoIdActor = 2**31 -1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 2**31 -1
        nuevoDescripcionActor = None
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 500 y id MAX . 
    def testModificarActorIdMaxDescripLen500(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 2**31 -1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 2**31 -1
        nuevoDescripcionActor = 'y'*500
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertTrue( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
    # La nueva descripci�n para el actor a modificar es tamaño 501 y id MAX . 
    def testModificarActorIdMaxDescripLen501(self):  
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        nuevoIdActor = 2**31 -1
        nuevoDescripcionActor = 'Esto es una prueba.'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'actor 1 ', nuevoDescripcionActor) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
          
        tempActor = clsActor()
        idactor = 2**31 -1
        nuevoDescripcionActor = 'y'*501
        result = tempActor.modificar( idactor,'Actor Nuevo' ,nuevoDescripcionActor )
        self.assertFalse( result )
        self.vaciarBaseDeDatos() # Se limpia la base de datos. 

    # FUNCION ELIMINAR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Eliminar el id de un actor que exista en la base de datos de un elemento. 
    def testEliminarIdActoresExist(self):
        self.vaciarBaseDeDatos()

        idProducto=1
        self.insertarProducto(idProducto)
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdActor = 1
        nuevoDescripcionActor = 'Esto es una prueba'
        nuevoActor = model.Actores( idProducto,nuevoIdActor,'Nombre Actor' ,nuevoDescripcionActor ) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 1
        query = tempActor.eliminar(idactor )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()

    # Eliminar el id de un actor con base de datos vacia
    def testEliminarIdActoresNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = 1000
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()

        
    # Eliminar el id de un actor con base de datos un elemento y busqueda no exitosa
        
    def testEliminarIdActoresNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        nuevoIdActor = 2
        nuevoDescripcionActor = 'Esto es una prueba'
        nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'Nombre Actor' ,nuevoDescripcionActor ) 
        model.db.session.add(nuevoActor)
        model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 1
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
        
    # Eliminar el id de un actor con base de datos de varios elemento y busqueda no exitosa   
    def testEliminarIdActoresNotExistVariosElementos(self):
        self.vaciarBaseDeDatos()    
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'Nombre Actor' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 5
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
          
    # Eliminar el id de un actor con base de datos de varios elemento y busqueda exitosa   
    def testEliminarIdActoresExistVariosElementos(self):
        self.vaciarBaseDeDatos()  
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        # Se insertaN elementoS en la base. Dicha insercion se asegura
        # que es valida.
        for indice in range(1,4,1):
            nuevoIdActor = indice
            nuevoDescripcionActor = 'Descripcion ' + str(indice)
            nuevoActor = model.Actores( nuevoIdProducto,nuevoIdActor,'Nombre Actor' ,nuevoDescripcionActor ) 
            model.db.session.add(nuevoActor)
            model.db.session.commit()   
        
        tempActor = clsActor()
        idactor = 3
        query = tempActor.eliminar( idactor )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del actor a Eliminar es un string.
    def testEliminarIdActoresString(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
 
        
        tempActor = clsActor()
        idactor = '1'
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)
        
        self.vaciarBaseDeDatos()
        
    # El id del actor a Eliminar es de tipo float.
    def testEliminarIdActoresFloat(self):
        self.vaciarBaseDeDatos()
        
        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = 1.01
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del actor a Eliminar es nulo.
    def testEliminarIdActoresNone(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)

        tempActor = clsActor()
        idactor = None
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del actor a Eliminar es negativo.
    def testEliminarIdActoresNegative(self):
        self.vaciarBaseDeDatos()

        nuevoIdProducto = 1
        self.insertarProducto(nuevoIdProducto)
        
        tempActor = clsActor()
        idactor = -3
        query = tempActor.eliminar( idactor )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  