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
    
    def testHistoriaExist(self):
        model.db.session.query(model.Historia_Usuario).delete()
        model.db.session.query( model.Pila ).delete() # Se limpia la base de datos
        tempHistoria = clsHistoria()
        self.assertIsNotNone(tempHistoria)
          
          
  # FUNCION BUSCAR

    ### CASOS VALIDOS (Casos Interiores).

    #Test 2: Buscar el codigo de historia que exista

    def find_CodHistoriaExist(self):       
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        #Se inserta un elemento valido en la base de datos
        newIdProducto = 1
        newDescripProducto=' Viendo mis casos de prueba  '
        newProducto = model.Pila(newIdProducto,newDescripProducto,"hola",1)
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        newcodHistoria = "c1"
        newTipoHostoria= "opcional"
        idHistoria=1
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        historiaIdPila= newIdProducto 
        newProducto = model.Historia_Usuario(idHistoria,newcodHistoria,historiaIdPila,newTipoHostoria,1,1)
        model.db.session.add(newProducto)
        model.db.session.commit()

        tempHistoria = clsHistoria()
        codHistoria = "c1"
        query = tempHistoria.find_CodHistoria(codHistoria)
        self.assertIsNotNone(query[0])
        model.db.session.query( model.Pila ).delete() # Se limpia la base de datos

    # Test 3: Buscar el codigo de historia que no existe
    def find_CodHistoriaNotExist(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempHistoria = clsHistoria()
        codHistoria = "c1"
        query = tempHistoria.find_CodHistoria(codHistoria)
        self.assertEqual(query,[])

    ### CASOS INVALIDOS ( Casos Malicia )

    # Test 4: El codigo es entero.
    def testfind_CodHistoriaInt(self):
        tempHistoria = clsHistoria()
        codHistoria = 1
        query = tempHistoria.find_CodHistoria(codHistoria)
        self.assertEqual(query,[])
    
    # Test 5: El codigo a buscar es de tipo float.
    def testfind_CodHistoriaFloat(self):
        tempHistoria = clsHistoria()
        codHistoria = 1.0
        query = tempHistoria.find_CodHistoria(codHistoria)
        self.assertEqual(query,[])  

    # Test 6: El codigo de la historia a buscar es nulo.
    def testfind_CodHistoriaNone(self):
        tempHistoria = clsHistoria()
        codHistoria = None
        query = tempHistoria.find_CodHistoria(codHistoria)
        self.assertEqual(query,[])

    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Insertar una historia
    def testinsert_Historia(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia(1,'codigo','Opcional',1,1,1)
        self.assertTrue(result)
        
        

    # Test 9: Se insertara una historia con codigo float.
    def testinsert_HistoriaCodFloat(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia(1,12.0,'Opcional',1,1,1)
        self.assertFalse(result[0])
                
    ### CASOS INVALIDOS( Casos Malicia ):    

    #Test 11: Se insertara una historia con tipo distinto y codigo entero.
    def testinsert_HistoriaTipoDistintoyCodInt(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia(salida[1],12,'tipoDistinto',1,1,1)
        self.assertFalse(result[0])

    # Test 12:  Se insertara una historia con tipo distinto y codigo float.
    def testinsert_HistoriaTipoDistintoyCodFloat(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia(salida[1],12.34,'tipoDistinto',1,1,1)
        self.assertFalse(result[0])

    #Test 13: Se insertara una historia con codigo None.
    def testinsert_HistoriaNone(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia(salida[1], None, 'Obligatorio',1,1,1)
        self.assertFalse(result[0])
        
    # FUNCION MODIFICAR
    # Casos Validos
    #Test :
    def testmodify_Historia(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        result = tempHistoria.modify_Historia(salida[1],1)
        self.assertTrue(result)
        
    def testmodify_IdProductNone(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = 1
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductStr(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = "Producto"
        IdHistoria = 1
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductEmpty(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = ""
        IdHistoria = 1
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductList(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = []
        IdHistoria = 1
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
    
    def testmodify_IdProductFLoat(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 2.5
        IdHistoria = 1
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        
    def testmodify_IdProductNegNum(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = -23
        IdHistoria = 1
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        self.assertFalse(result)
        
    def testmodify_IdHistoriaNone(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = None
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdHistoriaStr(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = "Historia"
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
    
    def testmodify_IdHistoriaEmpty(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = ""
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdHistoriaList(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = []
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdHistoriaFLoat(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = 2.5
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdHistoriaNegNum(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = -67
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductNoneIdHistoriaStr(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = "jajaja"
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
    
    def testmodify_IdProductNoneIdHistoriaNone(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = None
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductNoneIdHistoriaEmpty(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = ""
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductNoneIdHistoriaList(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = []
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductNoneIdHistoriaFloat(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = 2.5
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductNoneIdHistoriaNegNum(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = None
        IdHistoria = -456
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductStrIdHistoriaNone(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = "pruba1"
        IdHistoria = None
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductStrIdHistoriaEmpty(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = "prueba1"
        IdHistoria = ""
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductStrIdHistoriaList(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = "prueba1"
        IdHistoria = []
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductStrIdHistoriaFloat(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = "prueba1"
        IdHistoria = 5.7
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_IdProductStrIdHistoriaaNegNUm(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        idProducto = "prueba1"
        IdHistoria = -3445
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testmodify_Invalid(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        
        tempHistoria = clsHistoria()
        
        idProducto = 1
        IdHistoria = 23
        
        result = tempHistoria.modify_Historia(idProducto,IdHistoria)
        self.assertFalse(result)
        
    def testfindHistoria(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        tempHistoria = clsHistoria()
        
        IdHistoria = 1
        result = tempHistoria.find_Historia(IdHistoria)
        self.assertIsNotNone(result)
        
    def testfindHistoriaIdHistoriaNone(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = None
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])
        
        
    def testfindHistoriaIdHistoriaStr(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = "hola"
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])
        
    def testfindHistoriaIdHistoriaEmpty(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = ""
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])
        
    def testfindHistoriaIdHistoriaList(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = []
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])
        
    def testfindHistoriaIdHistoriaFLoat(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = 2.4
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])
        
    def testfindHistoriaIdHistoriaNegNum(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = -4
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])
        
    def testfindHistoriaIdHistoriaInvalid(self):
        
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Acciones).delete()
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos
        
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1','hola',1)
        
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        
        newHistoriaUsuario = model.Historia_Usuario(1,"codigo", 1, "opcional", 1,1,1)
        model.db.session.add(newHistoriaUsuario)
        model.db.session.commit() 
        
        tempHistoria = clsHistoria()
        
        IdHistoria = 24
        query = tempHistoria.find_Historia(IdHistoria)
        self.assertEqual(query,[])