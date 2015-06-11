# -*- coding: utf-8 -*-

"""
    UNIVERSIDAD SIMÓN BOLÍVAR
    Departamento de Computación y Tecnología de la Información.
    CI-3715 - Ingeniería de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Equipo SoftDev

    DESCRIPCION: 
        Módulo que contiene los métodos que permitirán insertar, modificar y
        eliminar objetivos del producto.
"""

from flask import request, session, Blueprint, json
from app.scrum.funcObjetivo import clsObjetivo
from app.scrum.controlDeAcceso import clsControlDeAcceso
from model import db, Objetivos

objetivo = Blueprint('objetivo', __name__)

#.-----------------------------------------------------------------------------.

@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():

    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, 
               {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    # Parámetros del objetivo a crear.
    descripcion = params.get('descripcion', None)
    transversalidad = params.get('transversal', None)

    if ( (transversalidad != None) and (descripcion!= None)):
        controlDeAcceso = clsControlDeAcceso()
        descripcionValida = controlDeAcceso.verificarDescripcion( descripcion )

        if ( descripcionValida ):
            nuevoObjetivo = clsObjetivo()
            creacionCorrecta = nuevoObjetivo.insertar(idProducto, descripcion,
                                                      transversalidad)
            if ( creacionCorrecta ):
                res = results[0]  
                # Se actualiza el URL de la pág a donde se va a redirigir.
                res['label'] = res['label'] + '/' + str(idProducto) 

    res['idPila'] = idProducto

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.
@objetivo.route('/objetivo/AElimObjetivo')
def AElimObjetivo():
    #GET parameter
    identificador = int(session['idObjetivo'])
    idProducto = int(session['idPila'])
    results = [{'label':'/VProducto', 'msg':['Objetivo eliminado']}, {'label':'/VObjetivo', 'msg':['No se pudo eliminar este objetivo']}, ]
    res = results[1]

    objetivo = clsObjetivo()
    eliminarCorrecto = objetivo.eliminar(identificador)

    if(eliminarCorrecto):
        res = results[0]
        res['label'] = res['label'] + '/' + str(idProducto)

    if (res == results[1]):
        res['label'] = res['label'] + '/' + str(identificador)
    

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():

    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, 
                {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[1]
    
    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    # Se obtiene los atributos del objetivo a modificar.
    identificador = int (params.get('idObjetivo',1))
    descripcion = params.get('descripcion', None)
    transversalidad = params.get('transversal', None)

    if ((transversalidad != None) and (descripcion != None)):
        objetivo = clsObjetivo()
        modificacionCorrecta  = objetivo.modificar(identificador, descripcion, 
                                                   transversalidad)
        if ( modificacionCorrecta ):
            res = results[0]
            res['label'] = res['label'] + '/' + str(idProducto)

    # Se actualiza el URL de la pág a donde se va a redirigir.
    if (res == results[1]):
        res['label'] = res['label'] + '/' + str(identificador)
    res['idPila'] = idProducto   

    session['idObjetivo'] = identificador

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
   
    # Producto actual.
    idProducto = session['idPila']

    res['fObjetivo_opcionesTransversalidad'] = [
        {'key':0, 'value':'No'},  
        {'key':1, 'value':'Si'},]

    # Se almacena la información recibida.
    res['fObjetivo'] = {'idPila': idProducto,
                        'idObjetivo':request.args.get('idObjetivo',1),
                        'descripcion':request.args.get('descripcion',''),
                        'transversal':request.args.get('transversal',0)}
    res['idPila'] = idProducto

    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    identificador = int(request.args.get('idObjetivo',1))
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']


    idProducto = int(request.args.get('idPila',1))

    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador del objetivo actual.
    
    res['idObjetivo'] = identificador

    # Se obtiene la información del objetivo a modificar.
    objetivoBuscado = db.session.query(Objetivos).\
                        filter(Objetivos.identificador == identificador).\
                        first()
    descripcion = objetivoBuscado.descripcion
    transversalidad = objetivoBuscado.transversalidad

    # Se almacena la información a enviar.
    res['fObjetivo'] = {'idPila': idProducto,
                        'idObjetivo':identificador,
                        'descripcion':descripcion,
                        'transversal':transversalidad}

    res['fObjetivo_opcionesTransversalidad'] = [
        {'key':0, 'value':'No'},
        {'key':1, 'value':'Si'},]

    return json.dumps(res)

#.-----------------------------------------------------------------------------.