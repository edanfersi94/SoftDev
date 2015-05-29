"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcActor.py"
    
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
    
             
    def testHistActoresExist(self):
        
        model.db.session.query( model.ActoresHistorias).delete()  # Se limpia la base de datos.
        model.db.session.query( model.Historia_Usuario ).delete()
        model.db.session.query( model.Actores).delete()
        model.db.session.query( model.Pila).delete() 
        
        NewIdPila = 1
        NewdescripProducto = "PruebaPila"
        
        NewIdHistActor = 1
        NewIdHistoria  = 1
        NewtipoHistoria_Usuario = "Opcional"
        NewCodigoHistoria_Usuario = "codigo1"
        NewId_Pila_Historia_Usuario = 1
        NewId_Acciones_Historia_Usuario = 1
        
        NewId_actores = 1
        Newnombre_actores = "Nombre Actor"
        Newdescripcion_actores = "Descripcion Actor"
        NewidProducto = 1
        
        newPila = model.Pila(NewIdPila, NewdescripProducto)
        model.db.session.add(newPila)
        model.db.session.commit()
        
        newActor = model.Actores(NewidProducto, NewId_actores, Newnombre_actores,Newdescripcion_actores)
        model.db.session.add(newActor)
        model.db.session.commit()
        
        newHistoria = model.Historia_Usuario(NewIdHistoria,NewCodigoHistoria_Usuario,NewCodigoHistoria_Usuario, NewId_Pila_Historia_Usuario, NewtipoHistoria_Usuario,NewId_Acciones_Historia_Usuario)
        model.db.session.add(newHistoria)
        model.db.session.commit()
        
        resultInsert = tempHistActor. insert_Actor(NewIdHistActor,NewIdActores)
        self.assertTrue(resultInsert)
        