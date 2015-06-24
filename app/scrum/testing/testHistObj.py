"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcHistObjetivo.py"
    
"""

#--------------------------------------------------------------------------------------

# Librerias a utilizar
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

# PATH que permite utilizar al modulo "funcHistObjetivo.py"
sys.path.append('../')
from funcHistObjetivo import clsHistoriaObj

import unittest


class TestHistObj(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query(model.ObjHistorias).delete()
        model.db.session.query(model.Historias).delete()
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Objetivos).delete()
        model.db.session.query(model.Actores).delete()
        model.db.session.query(model.Productos).delete()
        
    #Funcion que inserta datos las tablas que se necesitan para poder insertar datos a la tabla "objHistorias"
    
    def insertar(self):
        
        #Datos a ingresar a la tabla de pila
        NewIdPila = 1
        NewdescripProducto = "PruebaPila1"
        
        #Se ingresa manualmente los datos a la tabla pila
        newPila = model.Productos(NewIdPila, "prod",NewdescripProducto,1)
        model.db.session.add(newPila)
        model.db.session.commit()
        
        
        #Datos a ingresar a la tabla actor
        NewidObjetivo = 1
        NewdescripObjetivo = "Descrip Objetivo"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla objetivos
        newObjetivo = model.Objetivos(NewidProducto, NewidObjetivo,NewdescripObjetivo,0)
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        
        #Datos a ingresar a la tabla accion
        Newidaccion = 1
        NewdescripAccion = "Descrip Accion"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla acciones
        newAccion = model.Acciones(NewidProducto, Newidaccion, NewdescripAccion)
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        
        #Datos a ingresar a la tabla de historia
        NewIdHistObj = 1
        NewIdHistoria  = 1
        NewtipoHistoria_Usuario = 1
        NewCodigoHistoria_Usuario = "codigo1"
        NewId_Pila_Historia_Usuario = 1
        NewId_Acciones_Historia_Usuario = 1
        NewSuper = 1
        
        #Se ingresa manualmente los datos a la tabla historia
        newHistoria = model.Historias(NewIdHistoria,NewCodigoHistoria_Usuario, NewId_Pila_Historia_Usuario,NewtipoHistoria_Usuario, NewId_Acciones_Historia_Usuario,NewSuper,1)
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # test1:Insertar una objetivo-historia  en la base de datos.
    
    #---------------------------------------------------------------------------------------------------------------------         
    def testHistObjetivoExist(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewIdObj = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewIdObj)
        self.assertTrue(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #--------------------------------------------------------------------------------------
        
    ### CASOS INVALIDOS( Casos Malicia ):
    
    #---------------------------------------------------------------------------------------------------------------    
    # test2: Se inserta un idHistoria de tipo float
    #                idObjetivo de tipo int
        
    def testInsertarIdHistoriaFloat(self):
        
       
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1.2
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #--------------------------------------------------------------------------------------------------------------------------   
    
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test3: Se inserta un idHistoria de tipo string
    #                idObjetivo de tipo int
    def testInsertarIdHistoriaStr(self):
    
       #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = "Hola"
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #-----------------------------------------------------------------------------------------------
        
    #---------------------------------------------------------------------------------------------------
    # test4: Se inserta un idHistoria de tipo None
    #                idObjetivo de tipo int
        
    def testInsertarIdHistoriaNone(self):
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = None
        NewidObjetivo= 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        # -----------------------------------------------------------------------------
    
    # test5: Se inserta un idHistoria vacio
    #                idObjetivo de tipo int 
    
    def testInserIdhistoriaEmpty(self):
       
       #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = ''
        NewidObjetivoes = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivoes)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
        
    # test6: Se inserta un idHistoria negativo
    #                idObjetivo de tipo int
    
    def testInsertarIdHistoriaNeg(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test7: Se inserta un idHistoria float negativo
    #                idObjetivo de tipo int
    
    
    def testInsertarIdHistoriaNegFLoat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2.3
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test8: Se inserta un idHistoria de tipo string con una cardinalidad de 2**31 -1
    #                idObjetivo de tipo in
    
    #def testInsertarIdHistoriaStrMax(self):
        
        #Limpia bases de datos
        #self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        #self.insertar()
        
        #tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
    #    NewIdHistObj = 'z'*(2**31-1)
    #    NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
    #    resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test9: Se inserta un idHistoria de tipo int
    #                      idObjetivo de tipo string
    def testInsertarIdObjetivoStr(self):
    
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = "holaaaa"
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #---------------------------------------------------------------------------------------------
        
    # test10: Se inserta un idHistoria de tipo int
    #                idObjetivo de tipo float
        
    def testInsertaridObjetivoFloat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = 1.1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------
        
    # test11: Se inserta un idHistoria de tipo int
    #                idObjetivo de tipo NOne
        
    def testInsertaridObjetivoNone(self):
        
       #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = None
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #------------------------------------------------------------------------------------------
        
    
        #--------------------------------------------------------------------------------
        
    # test12: Se inserta un idHistoria int
    #                idObjetivo de tipo negativo
    
    def testInsertaridObjetivoNeg(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = -31
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test13: Se inserta un idHistoria int
    #                idObjetivo de tipo float neagativo
    
    
    def testInsertaridObjetivoNegFLoat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = -2.5
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test14: Se inserta un idHistoria de tipo int
    #                idObjetivo de tipo string con una cardinalidad de 2**31 -1
    
    #def testInsertarObjetivoStrMax(self):
        
        #Limpia bases de datos
        #self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        #self.insertar()
        
        #tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
    #    NewIdHistObj = 1
    #    NewidObjetivo = 'z'*(2**31-1)
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
    #    resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------------------------    
    # test15: Se inserta un idHistoria de tipo float
    #                idObjetivo de tipo float
        
    def testInsertarIdFloat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1.2
        NewidObjetivo = 1.9
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #--------------------------------------------------------------------------------------------------------------------------   
    
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test16: Se inserta un idHistoria de tipo string
    #                idObjetivo de tipo float
    def testInsertarIdfloatStr(self):
    
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = "Hola"
        NewidObjetivo = 7.9
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #-----------------------------------------------------------------------------------------------
        
    #---------------------------------------------------------------------------------------------------
    # test17: Se inserta un idHistoria de tipo None
    #                idObjetivo de tipo None
        
    def testInsertarIdNone(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = None
        NewidObjetivo = None
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        # -----------------------------------------------------------------------------
    
    # test18: Se inserta un idHistoria vacio
    #                idObjetivo de tipo vacio 
    
    def testInserIdEmpty(self):
        tempObj = clsHistoriaObj()
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = ''
        NewidObjetivo = ''
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
        
    # test19: Se inserta un idHistoria negativo
    #                idObjetivo de tipo negativo
    
    def testInsertarIdNeg(self):
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2
        NewidObjetivo =-61
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test20: Se inserta un idHistoria float negativo
    #                idObjetivo de tipo string
    
    
    def testInsertarIdStrNegFLoat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2.3
        NewidObjetivo = "gogogogog"
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test21: Se inserta un idHistoria de tipo string con una cardinalidad de 2**31 -1
    #                idObjetivo de tipo string con una cardinalidad de 2**31 -1
    
    #def testInsertarIdHistoriaStrMax(self):
        
    #Limpia bases de datos
        #self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        #self.insertar()
        
        #tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
    #    NewIdHistObj = 'z'*(2**31-1)
    #    NewidObjetivo = 'u'*(2**31-1)
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
    #    resultInsert = tempObj.insertar(NewIdHistObj,NewidObjetivo)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
    
    # FUNCION ELIMINAR
    
  # Se quiere eliminar un objetivo que no esta    
    def testEliminarNotExist(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.eliminar(NewIdHistObj)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
  # Se quiere eliminar un objetivo que esta en la base de datos
    def testEliminarExist(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        
        tempObj = clsHistoriaObj()
        tempObj.insertar(NewIdHistObj,1)

        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.eliminar(NewIdHistObj)
        self.assertTrue(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
    
  # Se quiere eliminar un objetivo con id None que esta en la base de datos
    def testEliminarIdNone(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        
        tempObj = clsHistoriaObj()
        tempObj.insertar(NewIdHistObj,1)

        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.eliminar(None)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
    
  # Se quiere eliminar un objetivo con id String que esta en la base de datos
    def testEliminarIdString(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        
        tempObj = clsHistoriaObj()
        tempObj.insertar(NewIdHistObj,1)

        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.eliminar('None')
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
  # Se quiere eliminar un objetivo con id negativo que esta en la base de datos
    def testEliminarIdNegative(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        
        tempObj = clsHistoriaObj()
        tempObj.insertar(NewIdHistObj,1)

        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.eliminar(-1)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
  # Se quiere eliminar un objetivo con id float que esta en la base de datos
    def testEliminarIdFloat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        
        tempObj = clsHistoriaObj()
        tempObj.insertar(NewIdHistObj,1)

        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.eliminar(1.32)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 


    