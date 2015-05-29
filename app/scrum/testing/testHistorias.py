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
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        #Se inserta un elemento valido en la base de datos
        newIdProducto = 1
        newDescripProducto='ola k ase? Viendo mis casos de prueba o k ase? '
        newProducto = model.Pila(newIdProducto,newDescripProducto)
        model.db.session.add(newProducto)
        model.db.session.commit()
        
        newcodHistoria = "c1"
        newTipoHostoria= "opcional"
        idHistoria=1
        
        historiaIdPila= newIdProducto 
        newProducto = model.Historia_Usuario(idHistoria,newTipoHostoria,newcodHistoria,historiaIdPila)
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
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('Opcional','codigo',salida[1])
        self.assertTrue(result)
        
           
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 8: Se insertara una historia con codigo entero.
    def testinsert_HistoriaCodInt(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('Opcional',12,salida[1])
        self.assertFalse(result)

    # Test 9: Se insertara una historia con codigo float.
    def testinsert_HistoriaCodFloat(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('Opcional',12.0,salida[1])
        self.assertFalse(result)
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 10: Se insertara una historia con un tipo distinto.
    def testinsert_HistoriaTipoDistinto(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('tipoDistinto',"c12",salida[1])
        self.assertFalse(result)

    # Test 11: Se insertara una historia con tipo distinto y codigo entero.
    def testinsert_HistoriaTipoDistintoyCodInt(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('tipoDistinto',12,salida[1])
        self.assertFalse(result)

    # Test 12:  Se insertara una historia con tipo distinto y codigo float.
    def testinsert_HistoriaTipoDistintoyCodFloat(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('tipoDistinto',12.34,salida[1])
        self.assertFalse(result)

    # Test 13: Se insertara una historia con codigo None.
    def testinsert_HistoriaNone(self):
        model.db.session.query(model.Historia_Usuario).delete()  # Se limpia la base de datos.
        model.db.session.query(model.Pila).delete()  # Se limpia la base de datos.
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('Obligatoria',None,salida[1])
        self.assertFalse(result)

          
          
