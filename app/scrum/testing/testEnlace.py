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
        
    def insertarEnlace (self):
        idEnlace = 1
        idproducto = 1
        idclave = 1
        idvalor= 1
        
        newEnlace = model.Enlaces(idEnlace,idproducto,idclave,idvalor)
        model.db.session.add(newEnlace)
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
    
    #CASOS INVALIDOS
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
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = 345446
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insert_Enlace(idproducto,idSuper)
        self.assertFalse(result)
        
    # --------------------------------------------------------------------------------------
        
    # FUNCION MODIFICAR
    
    # CASO VALIDO
    
    #test: Modifica un enlace con los parametros correctos
    def testmodifyValid(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto =1
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertTrue(result)
        
    #CASOS INVALIDOS
    
    #test: Modifica un enlace con idProducto de tipo None, los demas parametros son de tipo entero
    def testmodifyIdProductoNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto =None
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idProducto de tipo String, los demas parametros son de tipo entero
    def testmodifyIdProductoString(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = "Hola"
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idProducto de tipo Empty, los demas parametros son de tipo entero
    def testmodifyIdProductoEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = ""
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idProducto de tipo List, los demas parametros son de tipo entero
    def testmodifyIdProductoList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = []
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idProducto de tipo Float, los demas parametros son de tipo entero
    def testmodifyIdProductoFLoat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 2.5454
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idProducto de tipo Numeros negativos, los demas parametros son de tipo entero
    def testmodifyIdProductoNegNum(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = -3.454
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idProducto que no exista, los demas parametros son de tipo entero
    def testmodifyIdProductoNoExist(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 34343
        viejoSuper = 1
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con viejorSuper de tipo None, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = None
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con viejorSuper de tipo String, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperString(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = "hola"
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con viejorSuper de tipo Empty, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = ""
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con viejorSuper de tipo List, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = []
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con viejorSuper de tipo Float, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperFloat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 2.3443
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
    
    #test: Modifica un enlace con viejorSuper de tipo numero negativos, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperNegNum(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = -23.44
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con viejorSuper que no exista, los demas parametros son de tipo entero
    def testmodifyIdviejoSuperNoExist(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 345464
        nuevoSuper = 2
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con nuevoSuper de tipo None, los demas parametros son de tipo entero
    def testmodifyIdnuevoSuperNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = None
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con nuevoSuper de tipo Empty, los demas parametros son de tipo entero
    def testmodifyIdnuevoSuperEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = ""
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con nuevoSuper de tipo String, los demas parametros son de tipo entero
    def testmodifyIdnuevoSuperString(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = "hola"
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con nuevoSuper de tipo List, los demas parametros son de tipo entero
    def testmodifyIdnuevoSuperList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = []
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con nuevoSuper de tipo Float, los demas parametros son de tipo entero
    def testmodifyIdnuevoSuperFloat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 2.3343
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con nuevoSuper de tipo Numeros negativos, los demas parametros son de tipo entero
    def testmodifyIdnuevoSuperNumNeg(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = -2.3434
        valor = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idValor de tipo None, los demas parametros son de tipo entero
    def testmodifyIdValorNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 1
        valor = None
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idValor de tipo Empty, los demas parametros son de tipo entero
    def testmodifyIdValorEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 1
        valor = ""
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idValor de tipo String, los demas parametros son de tipo entero
    def testmodifyIdValorString(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 1
        valor = "Hola"
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
        
    #test: Modifica un enlace con idValor de tipo List, los demas parametros son de tipo entero
    def testmodifyIdValorList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 1
        valor = []
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idValor de tipo Float, los demas parametros son de tipo entero
    def testmodifyIdValorFloat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 1
        valor = 2.333
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
    #test: Modifica un enlace con idValor de tipo Numeros Negativos, los demas parametros son de tipo entero
    def testmodifyIdValorNumNeg(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        self.insertarEnlace()
        
        idproducto = 1
        viejoSuper = 1
        nuevoSuper = 1
        valor = -223.333
        tempEnlace = clsEnlace()
        
        result = tempEnlace.modify_Enlace(idproducto,viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        
        
        
        
    