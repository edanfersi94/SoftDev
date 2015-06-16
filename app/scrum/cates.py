# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        Módulo que contiene las aplicaciones y vistas correspondientes a las
        categorias.
"""

#.-----------------------------------------------------------------------------.

from flask import request, session, Blueprint, json
from app.scrum.funcCategoria import clsCategoria
from model import db,Categorias

cates = Blueprint('cates', __name__)


@cates.route('/cates/ACrearCategoria', methods=['POST'])
def ACrearCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría creada.']}, {'label':'/VCategorias', 'msg':['Error al intentar crear categoría.']}, ]
    res = results[1]
    
    print("params",params)
    
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AElimCategoria')
def AElimCategoria():
    #GET parameter
    idCategoria = int(request.args['idCategoria'])
    results = [{'label':'/VCategorias', 'msg':['Categoría eliminada.']}, {'label':'/VCategorias', 'msg':['Error al intentar eliminar categoría.']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/' + str(idCategoria)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/AModifCategoria', methods=['POST'])
def AModifCategoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría actualizada.']}, {'label':'/VCategorias', 'msg':['Error al intentar modificar categoría.']}, ]
    res = results[1]
    #Action code goes here, res should be a list with a label and a message
    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cates.route('/cates/VCategoria')
def VCategoria():
    #GET parameter
    idCategoria = request.args['idCategoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['idCategoria'] = int(idCategoria)
    res['fCategoria'] = {'idCategoria':1, 'peso':3, 
                         'nombre':'Reparacíon edl motor'}


    #Action code ends here
    return json.dumps(res)



@cates.route('/cates/VCategorias')
def VCategorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    res['usuario'] = session['usuario']
    res['data0'] = [
      {'idCategoria':1, 'peso':1, 'nombre':'Reparación del parachoques' },
      {'idCategoria':2, 'peso':2, 'nombre':'Reparación de la carrocería' },
      {'idCategoria':3, 'peso':3, 'nombre':'Reparación del motor' },
    ]

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

