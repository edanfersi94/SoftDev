"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcHistActor.py"
    
"""

#--------------------------------------------------------------------------------------

# Librerias a utilizar
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

# PATH que permite utilizar al modulo "funcActor.py"
sys.path.append('../')
from funcHistActores import clsHistoriaActores

import unittest


class TestHistActor(unittest.TestCase):
    
    # FUNCION AUXILIAR
    
    def vaciarBaseDeDatos(self):
        model.db.session.query(model.ActoresHistorias).delete()
        model.db.session.query(model.Historia_Usuario).delete()
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Actores).delete()
        model.db.session.query(model.Pila).delete()
        
    def insertarPila(self):
        #Datos a ingresar a la tabla de pila
        NewIdPila = 1
        NewdescripProducto = "PruebaPila1"
        
        #Se ingresa manualmente los datos a la tabla pila
        newPila = model.Pila(NewIdPila, NewdescripProducto)
        model.db.session.add(newPila)
        model.db.session.commit()
        
    def insertarActor(self):
        
        #Datos a ingresar a la tabla actor
        Newidactor = 1
        newNombreActor = "Nombre Actor"
        NewdescripActor = "Descrip Actor"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla actores
        newActor = model.Actores(NewidProducto, Newidactor,newNombreActor,  NewdescripActor)
        model.db.session.add(newActor)
        model.db.session.commit()
        
    def insertarAccion(self):
        #Datos a ingresar a la tabla accion
        Newidaccion = 1
        NewdescripAccion = "Descrip Accion"
        NewidProducto = 1
        
        #Se ingresa manualmente los datos a la tabla acciones
        newAccion = model.Acciones(NewidProducto, Newidaccion, NewdescripAccion)
        model.db.session.add(newAccion)
        model.db.session.commit()
        
    def insertarHistoria(self):
        #Datos a ingresar a la tabla de historia
        NewIdHistActor = 1
        NewIdHistoria  = 1
        NewtipoHistoria_Usuario = "Opcional"
        NewCodigoHistoria_Usuario = "codigo1"
        NewId_Pila_Historia_Usuario = 1
        NewId_Acciones_Historia_Usuario = 1
        
        #Se ingresa manualmente los datos a la tabla historia
        newHistoria = model.Historia_Usuario(NewIdHistoria,NewCodigoHistoria_Usuario, NewId_Pila_Historia_Usuario, NewtipoHistoria_Usuario,NewId_Acciones_Historia_Usuario)
        model.db.session.add(newHistoria)
        model.db.session.commit()
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
        
        
        
        
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    
    
    ### CASOS VALIDOS( Casos Interiores ).
    # test1:Insertar una accion-historia  en la base de datos.
    
    #---------------------------------------------------------------------------------------------------------------------         
    def testHistActoresExist(self):
        
    
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertTrue(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #-----------------------------------------------------------------------------------------------------------------------------   
        
    ### CASOS INVALIDOS( Casos Malicia ):
    
    #---------------------------------------------------------------------------------------------------------------    
    # test2: Se inserta un idHistoria de tipo float
    #                idActor de tipo int
        
    def testinsertIdHistoriaFloat(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1.2
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #--------------------------------------------------------------------------------------------------------------------------   
    
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test3: Se inserta un idHistoria de tipo string
    #                idActor de tipo int
    def testInsertIdHistoriaStr(self):
    
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = "Hola"
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #-----------------------------------------------------------------------------------------------
        
    #---------------------------------------------------------------------------------------------------
    # test4: Se inserta un idHistoria de tipo None
    #                idActor de tipo int
        
    def testInsertIdHistoriaNone(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = None
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        # -----------------------------------------------------------------------------
    
    # test5: Se inserta un idHistoria vacio
    #                idActor de tipo int 
    
    def testInserIdhistoriaEmpty(self):
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = ''
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
        
    # test6: Se inserta un idHistoria negativo
    #                idActor de tipo int
    
    def testInsertIdHistoriaNeg(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = -2
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test7: Se inserta un idHistoria float negativo
    #                idActor de tipo int
    
    
    def testInsertIdHistoriaNegFLoat(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = -2.3
        NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test8: Se inserta un idHistoria de tipo string con una cardinalidad de 2**31 -1
    #                idActor de tipo in
    
    #def testInsertIdHistoriaStrMax(self):
        
    #    tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
    #    self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
    #    self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
    #    self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
    #    self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
    #    NewIdHistActor = 'z'*(2**31-1)
    #    NewIdActores = 1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
    #    resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test9: Se inserta un idHistoria de tipo int
    #                      idActor de tipo string
    def testInsertIActoresStr(self):
    
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1
        NewIdActores = "holaaaa"
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #---------------------------------------------------------------------------------------------
        
    # test10: Se inserta un idHistoria de tipo int
    #                idActor de tipo float
        
    def testinsertIdActoresFloat(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1
        NewIdActores = 1.1
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------
        
    # test11: Se inserta un idHistoria de tipo int
    #                idActor de tipo NOne
        
    def testInsertIdActorNone(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1
        NewIdActores = None
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #------------------------------------------------------------------------------------------
        
    
        #--------------------------------------------------------------------------------
        
    # test12: Se inserta un idHistoria int
    #                idActor de tipo negativo
    
    def testInsertIdActorNeg(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1
        NewIdActores = -31
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test13: Se inserta un idHistoria int
    #                idActor de tipo float neagativo
    
    
    def testInsertIdActorNegFLoat(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1
        NewIdActores = -2.5
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test14: Se inserta un idHistoria de tipo int
    #                idActor de tipo string con una cardinalidad de 2**31 -1
    
    #def testInsertActorStrMax(self):
        
    #    tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
    #    self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
    #    self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
    #    self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
    #    self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
    #    NewIdHistActor = 1
    #    NewIdActores = 'z'*(2**31-1)
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
    #    resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------------------------    
    # test15: Se inserta un idHistoria de tipo float
    #                idActor de tipo float
        
    def testinsertIdFloat(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = 1.2
        NewIdActores = 1.9
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
    #--------------------------------------------------------------------------------------------------------------------------   
    
        
    #------------------------------------------------------------------------------------------------------------------------------    
    # test16: Se inserta un idHistoria de tipo string
    #                idActor de tipo float
    def testInsertIdfloatStr(self):
    
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = "Hola"
        NewIdActores = 7.9
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #-----------------------------------------------------------------------------------------------
        
    #---------------------------------------------------------------------------------------------------
    # test17: Se inserta un idHistoria de tipo None
    #                idActor de tipo None
        
    def testInsertIdNone(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = None
        NewIdActores = None
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        # -----------------------------------------------------------------------------
    
    # test18: Se inserta un idHistoria vacio
    #                idActor de tipo vacio 
    
    def testInserIdEmpty(self):
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = ''
        NewIdActores = ''
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
        
    # test19: Se inserta un idHistoria negativo
    #                idActor de tipo negativo
    
    def testInsertIdNeg(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = -2
        NewIdActores =-61
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
        #--------------------------------------------------------------------------------
    
    # test20: Se inserta un idHistoria float negativo
    #                idActor de tipo string
    
    
    def testInsertIdStrNegFLoat(self):
        
        tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
        self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
        self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
        self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
        NewIdHistActor = -2.3
        NewIdActores = "gogogogog"
        
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
        resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
        self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
        self.vaciarBaseDeDatos() 
        
    # test21: Se inserta un idHistoria de tipo string con una cardinalidad de 2**31 -1
    #                idActor de tipo string con una cardinalidad de 2**31 -1
    
    #def testInsertIdHistoriaStrMax(self):
        
    #    tempHistActor = clsHistoriaActores()
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
        #Se añade una fila a la bases de datos de pila
    #    self.insertarPila()
        
        #Se añade una fila a la bases de datos de actores
    #    self.insertarActor()
        
        #Se añade una fila a la bases de datos de actores
    #    self.insertarAccion()
        
        #Se añade una fila a la bases de datos de historia
    #    self.insertarHistoria()
        
        #Datos a ingresar a la tabla actHistoria
    #    NewIdHistActor = 'z'*(2**31-1)
    #    NewIdActores = 'u'*(2**31-1)
        #Se llama a la funcion "insertActor" para que ingrese los datos a la bases de datos
    #    resultInsert = tempHistActor.insert_Actor(NewIdHistActor,NewIdActores)
    #    self.assertFalse(resultInsert)
        
        #Se limpia la bases de datos
    #    self.vaciarBaseDeDatos()
        
    #-------------------------------------------------------------------------------------------------------

        
        