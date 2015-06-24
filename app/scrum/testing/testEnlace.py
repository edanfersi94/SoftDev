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
        model.db.session.query(model.Actores).delete()
        model.db.session.query(model.Productos).delete()
    
    def InsertarProducto(self):
        #Datos a ingresar a la tabla de pila
        NuevoIdProducto = 1
        NuevoDescripcionProducto = "PruebaPila1"
        
        #Se ingresa manualmente los datos a la tabla pila
        nuevoProducto = model.Productos(NuevoIdProducto, NuevoDescripcionProducto,"hola",1)
        model.db.session.add(nuevoProducto)
        model.db.session.commit()
        
    def insertarEnlace (self):
        idEnlace = 1
        idproducto = 1
        idclave = 1
        idvalor= 1
        
        nuevoEnlace = model.Enlaces(idEnlace,idproducto,idclave,idvalor)
        model.db.session.add(nuevoEnlace)
        model.db.session.commit()
        
        
    #Se prueba que exista la clase clsEnlace
    def testEnlaceExist(self):
        model.db.session.query(model.Productos).delete()
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
        
        nuevoEnlace = model.Enlaces(idEnlace,idproducto,idclave,idvalor)
        model.db.session.add(nuevoEnlace)
        model.db.session.commit()
        self.vaciarBaseDeDatos()
    
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
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertTrue(result)
        self.vaciarBaseDeDatos()
    
    # test Se inserta un idProdicto de tipo None y idSuper de tipo int
    def testInsertarIdProductoNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = None
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProdicto de tipo String y idSuper de tipo int    
    def testInsertarIdProductoStr(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = "HOLA"
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProdicto vacio y idSuper de tipo int    
    def testInsertarIdProductoEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = ""
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
    
    # test Se inserta un idProdicto de tipo Lista y idSuper de tipo int    
    def testInsertarIdProductoList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = []
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
    
    # test Se inserta un idProdicto de tipo float y idSuper de tipo int    
    def testInsertarIdProductoFLoat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = 2.5656565
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProdicto de tipo numero entero negativo y idSuper de tipo int    
    def testInsertarIdProductoNegNum(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto =-34.0
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
    
    # test Se inserta un idProdicto de tipo int y idSuper de tipo None  
    def testInsertarIdSuperNone(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = None
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo String  
    def testInsertarIdSuperString(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = None
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProducto de tipo int y idSuper vacio 
    def testInsertarIdSuperEmpty(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = ""
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo List 
    def testInsertarIdSuperList(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = []
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo Float 
    def testInsertarIdSuperFLoat(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 2.454544
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # test Se inserta un idProducto de tipo int y idSuper de tipo Numeros Negativos 
    def testInsertarIdSuperNegNum(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = -2333.1
        idproducto = 1
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: El idProducto no se encuentra en la tabla Pila
    def testInsertarIdProductNoExist(self):
        
        #Se borra la base de datos
        self.vaciarBaseDeDatos()
        
        #Se introduce datos a la tabla producto
        self.InsertarProducto()
        
        idSuper = 1
        idproducto = 345446
        tempEnlace = clsEnlace()
        
        result = tempEnlace.insertar(idproducto,idSuper)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    # --------------------------------------------------------------------------------------
        
    # FUNCION MODIFICAR
    
    # CASO VALIDO
    
    #test: Modifica un enlace con los parametros correctos
    def testModificarValid(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertTrue(result)
        self.vaciarBaseDeDatos()
            
        
    #test: Modifica un enlace con viejorSuper de tipo None, los demas parametros son de tipo entero
    def testModificarIdviejoSuperNone(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con viejorSuper de tipo String, los demas parametros son de tipo entero
    def testModificarIdviejoSuperString(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con viejorSuper de tipo Empty, los demas parametros son de tipo entero
    def testModificarIdviejoSuperEmpty(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con viejorSuper de tipo List, los demas parametros son de tipo entero
    def testModificarIdviejoSuperList(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con viejorSuper de tipo Float, los demas parametros son de tipo entero
    def testModificarIdviejoSuperFloat(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
    
    #test: Modifica un enlace con viejorSuper de tipo numero negativos, los demas parametros son de tipo entero
    def testModificarIdviejoSuperNegNum(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con viejorSuper que no exista, los demas parametros son de tipo entero
    def testModificarIdviejoSuperNoExist(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con nuevoSuper de tipo None, los demas parametros son de tipo entero
    def testModificarIdnuevoSuperNone(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con nuevoSuper de tipo Empty, los demas parametros son de tipo entero
    def testModificarIdnuevoSuperEmpty(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con nuevoSuper de tipo String, los demas parametros son de tipo entero
    def testModificarIdnuevoSuperString(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con nuevoSuper de tipo List, los demas parametros son de tipo entero
    def testModificarIdnuevoSuperList(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con nuevoSuper de tipo Float, los demas parametros son de tipo entero
    def testModificarIdnuevoSuperFloat(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con nuevoSuper de tipo Numeros negativos, los demas parametros son de tipo entero
    def testModificarIdnuevoSuperNumNeg(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con idValor de tipo None, los demas parametros son de tipo entero
    def testModificarIdValorNone(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con idValor de tipo Empty, los demas parametros son de tipo entero
    def testModificarIdValorEmpty(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con idValor de tipo String, los demas parametros son de tipo entero
    def testModificarIdValorString(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
        
    #test: Modifica un enlace con idValor de tipo List, los demas parametros son de tipo entero
    def testModificarIdValorList(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con idValor de tipo Float, los demas parametros son de tipo entero
    def testModificarIdValorFloat(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
    #test: Modifica un enlace con idValor de tipo Numeros Negativos, los demas parametros son de tipo entero
    def testModificarIdValorNumNeg(self):
        
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
        
        result = tempEnlace.modificar(viejoSuper,nuevoSuper,valor)
        self.assertFalse(result)
        self.vaciarBaseDeDatos()
        
        
        
        
    