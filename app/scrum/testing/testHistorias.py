"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcHistoria.py"
    
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.
import os
import sys
from sqlalchemy.ext.baked import Result

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

sys.path.append('../')
from funcHistoria import clsHistoria
from funcProducto import clsProducto
from funcAccion import clsAccion

import unittest


class TestHistoria(unittest.TestCase):
    
    def vaciarBaseDeDatos(self):
        model.db.session.query(model.Historias).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Productos).delete()  # Se limpia la base de datos.
    
    def testHistoriaExist(self):
        model.db.session.query(model.Historias).delete()
        model.db.session.query( model.Productos).delete() # Se limpia la base de datos
        tempHistoria = clsHistoria()
        self.assertIsNotNone(tempHistoria)
                 

    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Insertar una historia
    def testinsert_Historia(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insertar(1,'codigo',1,1,0,1)
        self.assertTrue(result)
        self.vaciarBaseDeDatos()
        
        

    # Test 9: Se insertara una historia con codigo float.
    def testinsert_HistoriaCodFloat(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insertar(1,12.0,1,1,0,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos()
                
    ### CASOS INVALIDOS( Casos Malicia ):    

    #Test 11: Se insertara una historia con tipo distinto y codigo entero.
    def testinsert_HistoriaTipoDistintoyCodInt(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insertar(salida[1],12,'tipoDistinto',1,0,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos()

    # Test 12:  Se insertara una historia con tipo distinto y codigo float.
    def testinsert_HistoriaTipoDistintoyCodFloat(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insertar(salida[1],12.34,'tipoDistinto',1,0,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos()

    #Test 13: Se insertara una historia con codigo None.
    def testinsert_HistoriaNone(self):
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insertar(salida[1], None, 'Obligatorio',1,0,1)
        self.assertFalse(result[0])
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoria(self):
        
        self.vaciarBaseDeDatos()
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        IdHistoria = 1
        result = tempHistoria.buscarHistoria(IdHistoria)
        self.assertIsNotNone(result)
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoriaNone(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = None
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
        
    def testbuscarIdHistoriaStr(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = "hola"
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoriaEmpty(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = ""
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoriaList(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = None
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoriaFLoat(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = 2.4
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoriaNegNum(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = -4
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,None)
        self.vaciarBaseDeDatos()
        
    def testbuscarIdHistoriaInvalid(self):
        
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = 24
        query = tempHistoria.buscarHistoria(IdHistoria)
        self.assertEqual(query,[])
        self.vaciarBaseDeDatos()
        
  # FUNCION ELIMINAR
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Eliminar el id de una historia que exista en la base de datos de un elemento. 
    def testEliminarIdHistoriaExist(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 1
        query = tempHistoria.eliminar(idhistoria )
        self.assertTrue( query )
        self.vaciarBaseDeDatos()

    # Eliminar el id de una historia con base de datos vacia
    def testEliminarIdHistoriaNotExistBaseDeDatosVacia(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 1000
        query = tempHistoria.eliminar( idhistoria )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()

        
    # Eliminar el id de una historia con base de datos un elemento y busqueda no exitosa
        
    def testEliminarIdHistoriaNotExistOneElementos(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 13
        query = tempHistoria.eliminar( idhistoria )
        self.assertFalse(query)
        self.vaciarBaseDeDatos()
    
        
    ### CASOS INVALIDOS( Casos Malicia )
    #El id del historia a Eliminar es un string.
    def testEliminarIdHistoriaString(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
 
        
        tempHistoria = clsHistoria()
        idhistoria = '1'
        query = tempHistoria.eliminar( idhistoria )
        self.assertFalse(query)
        
        self.vaciarBaseDeDatos()
        
    # El id del historia a Eliminar es de tipo float.
    def testEliminarIdHistoriaFloat(self):
        self.vaciarBaseDeDatos()
        
        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria= clsAccion()
        idhistoria = 1.01
        query = tempHistoria.eliminar( idhistoria )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del historia a Eliminar es nulo.
    def testEliminarIdHistoriaNone(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 

        tempHistoria = clsHistoria()
        idhistoria = None
        query = tempHistoria.eliminar( idhistoria )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()

    #  El id del historia a Eliminar es negativo.
    def testEliminarIdHistoriaNegative(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = -3
        query = tempHistoria.eliminar( idhistoria )
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
    
    #.-------------------------------------------------------------------.  
  # FUNCION CAMBIAR PRIORIDADES
  
      #  El id del historia a cambiar no existe en la base de datos.
    def testCambiarPrioridadIdHistoriaNotExist(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 3
        prioridad=2
        query = tempHistoria.cambiarPrioridad(idhistoria, prioridad)
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
        
      #  El id del historia a cambiar existe en la base de datos.
    def testCambiarPrioridadIdHistoriaExist(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 1
        prioridad=2
        query = tempHistoria.cambiarPrioridad(idhistoria, prioridad)
        self.assertTrue(query)  
        self.vaciarBaseDeDatos()
  
        #  El id del historia a cambiar prioridad es float existe en la base de datos.
    def testCambiarPrioridadIdHistoriaPrioridadFloat(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 3
        prioridad=2.2
        query = tempHistoria.cambiarPrioridad(idhistoria, prioridad)
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
  
         #  El id del historia a cambiar prioridad es None existe en la base de datos.
    def testCambiarPrioridadIdHistoriaPrioridadNone(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 1
        prioridad=None
        query = tempHistoria.cambiarPrioridad(idhistoria, prioridad)
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
        
         #  El id del historia a cambiar prioridad es String existe en la base de datos.
    def testCambiarPrioridadIdHistoriaPrioridadString(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 1
        prioridad='error'
        query = tempHistoria.cambiarPrioridad(idhistoria, prioridad)
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
        
         #  El id del historia a cambiar prioridad es negativo existe en la base de datos.
    def testCambiarPrioridadIdHistoriaPrioridadNegative(self):
        self.vaciarBaseDeDatos()

        tempProducto = clsProducto()
        salida= tempProducto.insertar('Producto','Prueba de Producto1',1)
        
        tempAccion = clsAccion()
        tempAccion.insertar(1,"Holaaa")
        
        newHistoriaUsuario = model.Historias(1,"codigo", 1, 1, 1,0,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        idhistoria = 1
        prioridad=-3
        query = tempHistoria.cambiarPrioridad(idhistoria, prioridad)
        self.assertFalse(query)  
        self.vaciarBaseDeDatos()
  
