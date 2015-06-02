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
from funcAccion import clsAccion

import unittest


class TestHistoria(unittest.TestCase):
    
    def test1HistoriaExist(self):
        #model.db.session.query( model.pila).delete()
        tempProducto = clsProducto()
        tempProducto.insert_Producto('Prueba de Producto1')
        tempHistoria = clsHistoria()
        tempAccion = clsAccion()
        tempAccion.insert_Accion(1,"Holaaa")
        result = tempHistoria.insert_Historia(1,"codigo","opcional",1)
        self.assertTrue(result)

          # Se limpia la base de datos.
          
    def test3modify(self):
        tempHistoria = clsHistoria()
        find = tempHistoria.find_Historia(1)
        for f in find:
            tempHistoria.modify_Historia(1,1)
    
    def test2find(self):
        tempHistoria = clsHistoria()
        find = tempHistoria.find_Historia(1)