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

#.-----------------------------------------------------------------------------.

@cates.route('/cates/ACrearCategoria', methods=['POST'])
def ACrearCategoria():

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría creada.']}, 
               {'label':'/VCategorias', 'msg':['Error al intentar crear categoría.']}, ]
    res = results[1]
    
    nombre = params.get('nombre',None)
    peso = params.get('peso',None)   
    
    if (( nombre != None ) and ( peso != None )): 
        categoria = clsCategoria()
        creaccionCorrecta = categoria.insertar(nombre,peso)
        res = results[0] if creaccionCorrecta[0] else results[1]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@cates.route('/cates/AElimCategoria')
def AElimCategoria():
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    idCategoria = int(request.args['idCategoria'])
    results = [{'label':'/VCategorias', 'msg':['Categoría eliminada.']}, 
               {'label':'/VCategorias', 'msg':['Error al intentar eliminar categoría.']}, ]
    res = results[1]

    res['label'] = res['label'] + '/' + str(idCategoria)
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@cates.route('/cates/AModifCategoria', methods=['POST'])
def AModifCategoria():
  
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    params = request.get_json()
    results = [{'label':'/VCategorias', 'msg':['Categoría actualizada.']}, 
               {'label':'/VCategorias', 'msg':['Error al intentar modificar categoría.']}, ]
    # Resultado de la modificación de la categoría.
    res = results[1]
    
    identificador = int(session['idCategoria'])
    nombre = params.get('nombre', None)
    peso = params.get('peso', None)
    
    if ((nombre != None) and (peso != None )):
        categoria = clsCategoria()
        modificacionCorrecta = categoria.modificar(identificador, nombre, peso)    
        res = results[0] if modificacionCorrecta else results[1]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@cates.route('/cates/VCategoria')
def VCategoria():

    res = {}
    if "actor" in session:
        res['actor'] = session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    idActual = int(request.args.get('idCategoria',1))
    infoActual = Categorias.query.filter(Categorias.identificador == idActual).first()
    res['usuario'] = session['usuario']
    
    res['idCategoria'] = int(idActual)
    session['idCategoria'] = int(idActual)
    
    res['fCategoria'] = {'idCategoria':idActual, 'peso':infoActual.peso, 
                         'nombre':infoActual.nombre}
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@cates.route('/cates/VCategorias')
def VCategorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
  
    # Se muestra la lista de categorias.
    categorias = Categorias.query.all()
    
    if (categorias != None):
        categoria = clsCategoria()
        categoria.insertar('Implementar una acción',2)
        categoria.insertar('Implementar una vista',2)
        categoria.insertar('Implementar una regla de negocio o un método de una clase',2)
        categoria.insertar('Migrar la base de datos',2)
        categoria.insertar('Crear un diagrama UML',1)
        categoria.insertar('Crear datos iniciales',1)
        categoria.insertar('Crear una prueba de aceptación',1)
        categoria.insertar('Actualizar un elemento implementado en otra tarea',2)
        categoria.insertar('Actualizar en elemento implementado en otra tarea',1)
        categoria.insertar('Escribir el manual en línea de unapágina',1)
        
    res['usuario'] = session['usuario']
    res['data0'] = [
      {'idCategoria':cat.identificador, 'peso':cat.peso, 'nombre':cat.nombre }
      for cat in categorias]
    
    return json.dumps(res)

#.-----------------------------------------------------------------------------.