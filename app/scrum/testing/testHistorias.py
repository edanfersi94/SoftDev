"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcAccion.py"
    
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
        model.db.session.query( model.Pila ).delete() # Se limpia la base de datos
        tempProducto = clsProducto()
        salida= tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        result = tempHistoria.insert_Historia('Opcional','codigo',salida[1])
        self.assertTrue(result)
          # Se limpia la base de datos.