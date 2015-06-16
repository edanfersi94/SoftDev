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
    
    nombre = params.get('nombre',None)
    peso = params.get('peso',None)   
    
    if not(( nombre == None ) and ( peso == None )): 
        categoria = clsCategoria()
        creaccionCorrecta = categoria.insertar(nombre,peso)
        
        if( creaccionCorrecta[0]):
            res = results[0]
  
    
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
  
    categoriasBuscadas = db.session.query(Categorias).all()
    
    if (categoriasBuscadas == []):
        
        categoriaNueva = Categorias(1,'Implementar una acción',2)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(2,'Implementar una vista',2)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(3,'Implementar una regla de negocio o un método de una clase',2)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(4,'Migrar la bases de datos',2)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(5,'Crear un diagrama UML',1)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(6,'Crear datos iniciales',1)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(7,'Crear un criterio de aceptación',1)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(8,'Crear una prueba de aceptación',2)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(9,'Actualizar un elemento implementado en otra tarea',1)
        db.session.add(categoriaNueva)
        db.session.commit()
        
        categoriaNueva = Categorias(10,'Escribir el manual en línea de una página',1)
        db.session.add(categoriaNueva)
        db.session.commit()
        
    categorias = db.session.query(Categorias).all()
    res['usuario'] = session['usuario']
    res['data0'] = [
      {'idCategoria':cat.identificador, 'peso':cat.peso, 'nombre':cat.nombre }
      for cat in categorias]

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here

