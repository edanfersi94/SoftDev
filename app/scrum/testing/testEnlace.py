"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcEnlace.py"
    
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
from funcProducto import clsProducto
from funcEnlace import clsEnlace

import unittest

class TestEnlace(unittest.TestCase):
    
    def vaciarBaseDeDatos(self):
        model.db.session.query(model.Enlaces).delete()
        model.db.session.query(model.Pila).delete()
    
    def InsertarProducto(self):
        #Datos a ingresar a la tabla de pila
        NewIdPila = 1
        NewdescripProducto = "PruebaPila1"
        
        #Se ingresa manualmente los datos a la tabla pila
        newPila = model.Pila(NewIdPila, NewdescripProducto)
        model.db.session.add(newPila)
        model.db.session.commit()
        
    #Se prueba que exista la clase clsEnlace
    def testEnlaceExist(self):
        model.db.session.query(model.Pila).delete()
        model.db.session.query( model.Enlaces ).delete() # Se limpia la base de datos
        tempEnlace = clsEnlace()
        self.assertIsNotNone(tempEnlace)
        
    #-------------------------------------------------------------------------------------
    #FUNCION INSERTAR
    
    #CASO VALIDO
    #test ; Se inserta idProducto y IdSuper de tipo int
    
    def testEnlaceValid(self):
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idEnlace = 1
        idproducto = 1
        idclave = 1
        idvalor= 1
        
        newEnlace = model.Enlaces(idEnlace,idproducto,idclave,idvalor)
        model.db.session.add(newEnlace)
        model.db.session.commit()
    
    # test : Se inserta un idProducto y idSuper correctos
    def testinsertarValid(self):
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertTrue(result)
    
    # test Se inserta un idProdicto de tipo None y idSuper de tipo int
    def testinsertIdProductoNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = None
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProdicto de tipo String y idSuper de tipo int    
    def testinsertIdProductoStr(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = "HOLA"
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProdicto vacio y idSuper de tipo int    
    def testinsertIdProductoEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = ""
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
    
    # test Se inserta un idProdicto de tipo Lista y idSuper de tipo int    
    def testinsertIdProductoList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = []
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
    
    # test Se inserta un idProdicto de tipo float y idSuper de tipo int    
    def testinsertIdProductoFLoat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = 2.5656565
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProdicto de tipo numero entero negativo y idSuper de tipo int    
    def testinsertIdProductoNegNum(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto =-34.0
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
    
    # test Se inserta un idProdicto de tipo int y idSuper de tipo None  
    def testinsertIdSuperNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = None
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo String  
    def testinsertIdSuperString(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = None
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProducto de tipo int y idSuper vacio 
    def testinsertIdSuperEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = ""
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo List 
    def testinsertIdSuperList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = []
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo Float 
    def testinsertIdSuperFLoat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 2.454544
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo Numeros Negativos 
    def testinsertIdSuperNegNum(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = -2333.1
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    #test: El idProducto no se encuentra en la tabla Pila
    def testinsertIdProductNoExist(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = -2333.1
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = 345446
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)