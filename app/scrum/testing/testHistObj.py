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
        model.db.session.query(model.Historia_Usuario).delete()
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Objetivo).delete()
        model.db.session.query(model.Pila).delete()
        
    #Funcion que inserta datos las tablas que se necesitan para poder insertar datos a la tabla "objHistorias"
    
    def insertar(self):
        
        #Datos a ingresar a la tabla de pila
        NewIdPila = 1
        NewdescripProducto = "PruebaPila1"
        
        #Se ingresa manualmente los datos a la tabla pila
        newPila = model.Pila(NewIdPila, NewdescripProducto)
        model.db.session.add(newPila)
        model.db.session.commit()
        
        NewIdPila = 2
        NewdescripProducto = "PruebaPila2"
        
        #Se ingresa manualmente los datos a la tabla pila
        newPila = model.Pila(NewIdPila, NewdescripProducto)
        model.db.session.add(newPila)
        model.db.session.commit()
        
        #Datos a ingresar a la tabla actor
        NewidObjetivo = 1
        NewdescripObjetivo = "Descrip Objetivo"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla objetivos
        newObjetivo = model.Objetivo(NewidProducto, NewidObjetivo,NewdescripObjetivo)
        model.db.session.add(newObjetivo)
        model.db.session.commit()
        
        NewidObjetivo = 2
        NewdescripObjetivo = "Descrip Objetivo"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla objetivos
        newObjetivo = model.Objetivo(NewidProducto, NewidObjetivo,NewdescripObjetivo)
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
        
        Newidaccion = 2
        NewdescripAccion = "Descrip Accion2"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla acciones
        newAccion = model.Acciones(NewidProducto, Newidaccion, NewdescripAccion)
        model.db.session.add(newAccion)
        model.db.session.commit()
        
        #Datos a ingresar a la tabla de historia
        NewIdHistObj = 1
        NewIdHistoria  = 1
        NewtipoHistoria_Usuario = "Opcional"
        NewCodigoHistoria_Usuario = "codigo1"
        NewId_Pila_Historia_Usuario = 1
        NewId_Acciones_Historia_Usuario = 1
        
        #Se ingresa manualmente los datos a la tabla historia
        newHistoria = model.Historia_Usuario(NewIdHistoria,NewCodigoHistoria_Usuario, NewId_Pila_Historia_Usuario, NewtipoHistoria_Usuario,NewId_Acciones_Historia_Usuario)
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        
        NewIdHistObj = 2
        NewIdHistoria  = 2
        NewtipoHistoria_Usuario = "Obligatorio"
        NewCodigoHistoria_Usuario = "codigo2"
        NewId_Pila_Historia_Usuario = 1
        NewId_Acciones_Historia_Usuario = 2
        
        #Se ingresa manualmente los datos a la tabla historia
        newHistoria = model.Historia_Usuario(NewIdHistoria,NewCodigoHistoria_Usuario, NewId_Pila_Historia_Usuario, NewtipoHistoria_Usuario,NewId_Acciones_Historia_Usuario)
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
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewIdObj)
        self.assertTrue(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #--------------------------------------------------------------------------------------
        
    ### CASOS INVALIDOS( Casos Malicia ):
    
    #---------------------------------------------------------------------------------------------------------------    
    # test2: Se inserta un idHistoria de tipo float
    #                idObjetivo de tipo int
        
    def testinsertIdHistoriaFloat(self):
        
       
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1.2
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #--------------------------------------------------------------------------------------------------------------------------   
    
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test3: Se inserta un idHistoria de tipo string
    #                idObjetivo de tipo int
    def testInsertIdHistoriaStr(self):
    
       #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = "Hola"
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #-----------------------------------------------------------------------------------------------
        
    #---------------------------------------------------------------------------------------------------
    # test4: Se inserta un idHistoria de tipo None
    #                idObjetivo de tipo int
        
    def testInsertIdHistoriaNone(self):
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = None
        NewidObjetivo= 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
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
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivoes)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
        
    # test6: Se inserta un idHistoria negativo
    #                idObjetivo de tipo int
    
    def testInsertIdHistoriaNeg(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test7: Se inserta un idHistoria float negativo
    #                idObjetivo de tipo int
    
    
    def testInsertIdHistoriaNegFLoat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2.3
        NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test8: Se inserta un idHistoria de tipo string con una cardinalidad de 2**31 -1
    #                idObjetivo de tipo in
    
    #def testInsertIdHistoriaStrMax(self):
        
        #Limpia bases de datos
        #self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        #self.insertar()
        
        #tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
    #    NewIdHistObj = 'z'*(2**31-1)
    #    NewidObjetivo = 1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
    #    resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test9: Se inserta un idHistoria de tipo int
    #                      idObjetivo de tipo string
    def testInsertIdObjetivoStr(self):
    
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = "holaaaa"
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #---------------------------------------------------------------------------------------------
        
    # test10: Se inserta un idHistoria de tipo int
    #                idObjetivo de tipo float
        
    def testinsertidObjetivoFloat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = 1.1
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------
        
    # test11: Se inserta un idHistoria de tipo int
    #                idObjetivo de tipo NOne
        
    def testInsertidObjetivoNone(self):
        
       #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = None
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #------------------------------------------------------------------------------------------
        
    
        #--------------------------------------------------------------------------------
        
    # test12: Se inserta un idHistoria int
    #                idObjetivo de tipo negativo
    
    def testInsertidObjetivoNeg(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = -31
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test13: Se inserta un idHistoria int
    #                idObjetivo de tipo float neagativo
    
    
    def testInsertidObjetivoNegFLoat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1
        NewidObjetivo = -2.5
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test14: Se inserta un idHistoria de tipo int
    #                idObjetivo de tipo string con una cardinalidad de 2**31 -1
    
    #def testInsertObjetivoStrMax(self):
        
        #Limpia bases de datos
        #self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        #self.insertar()
        
        #tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
    #    NewIdHistObj = 1
    #    NewidObjetivo = 'z'*(2**31-1)
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
    #    resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------------------------    
    # test15: Se inserta un idHistoria de tipo float
    #                idObjetivo de tipo float
        
    def testinsertIdFloat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = 1.2
        NewidObjetivo = 1.9
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #--------------------------------------------------------------------------------------------------------------------------   
    
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test16: Se inserta un idHistoria de tipo string
    #                idObjetivo de tipo float
    def testInsertIdfloatStr(self):
    
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = "Hola"
        NewidObjetivo = 7.9
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #-----------------------------------------------------------------------------------------------
        
    #---------------------------------------------------------------------------------------------------
    # test17: Se inserta un idHistoria de tipo None
    #                idObjetivo de tipo None
        
    def testInsertIdNone(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = None
        NewidObjetivo = None
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
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
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
        
    # test19: Se inserta un idHistoria negativo
    #                idObjetivo de tipo negativo
    
    def testInsertIdNeg(self):
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2
        NewidObjetivo =-61
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test20: Se inserta un idHistoria float negativo
    #                idObjetivo de tipo string
    
    
    def testInsertIdStrNegFLoat(self):
        
        #Limpia bases de datos
        self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        NewIdHistObj = -2.3
        NewidObjetivo = "gogogogog"
        
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
        resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test21: Se inserta un idHistoria de tipo string con una cardinalidad de 2**31 -1
    #                idObjetivo de tipo string con una cardinalidad de 2**31 -1
    
    #def testInsertIdHistoriaStrMax(self):
        
    #Limpia bases de datos
        #self.vaciarBaseDeDatos()
        
        #Inserta tablas dependientes
        #self.insertar()
        
        #tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
    #    NewIdHistObj = 'z'*(2**31-1)
    #    NewidObjetivo = 'u'*(2**31-1)
        #Se llama a la funcion "insertObjetivo" para que ingrese los datos a la bases de datos
    #    resultInsert = tempObj.insert_Objetivo(NewIdHistObj,NewidObjetivo)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
    def testmodify(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertTrue(result)
        
    def testmodifyIdHistoriaNone(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= None
        idObjetivo =1
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdHistoriaString(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= "hola"
        idObjetivo =1
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdHistoriaEmpty(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= ""
        idObjetivo =1
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
    
    def testmodifyIdHistoriaList(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= []
        idObjetivo =1
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdHistoriaFloat(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 2.5
        idObjetivo =1
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdHistoriaNegNum(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= -34
        idObjetivo =1
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdObjetivoNone(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        idObjetivo = None
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdObjetivoStr(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        idObjetivo = "hola"
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdObjetivoEmpty(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        idObjetivo = ""
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdObjetivoList(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        idObjetivo = []
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdObjetivoFLoat(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        idObjetivo = 2.4
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyIdObjetivoNegNum(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        idObjetivo = -34
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
        
    def testmodifyInvalid(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 23
        idObjetivo = 45
        
        result = tempObj.modify_Objetivo(idHistoria,idObjetivo)
        self.assertFalse(result)
    
    def testfindObjetivo(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 1
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertIsNotNone(query)
        
    def testfindObjetivoIdHistoriaNone(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= None
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
        
    def testfindObjetivoIdHistoriaStr(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= "hola"
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
        
    def testfindObjetivoIdHistoriaEmpty(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= ""
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
        
    def testfindObjetivoIdHistoriaList(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= []
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
    
    def testfindObjetivoIdHistoriaFLoat(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 2.5
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
        
    def testfindObjetivoIdHistoriaNegNum(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= -45
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
        
    def testfindObjetivoInvalid(self):
        self.vaciarBaseDeDatos()
        #Inserta tablas dependientes
        self.insertar()
        
        tempObj = clsHistoriaObj()
        
        #Datos a ingresar a la tabla objHistorias
        num_objInsertado =1
        idHistoria= 1
        idObjetivo =1
        
        newObj = model.ObjHistorias(num_objInsertado ,idHistoria, idObjetivo)
        model.db.session.add(newObj)
        model.db.session.commit()
        
        idHistoria= 354
        
        query = tempObj.find_Objetivo(idHistoria)
        self.assertEqual(query,[])
        
    