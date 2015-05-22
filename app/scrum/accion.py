# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcAccion import clsAccion
import model


accion = Blueprint('accion', __name__)

#.----------------------------------------------------------------------------------------.

@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]
    res = results[0]
    
    nueva_descripcion_acciones = params['descripcion']

    nuevaAccion = clsAccion()
    resultInset = nuevaAccion.insert_Accion( nueva_descripcion_acciones)

    if ( resultInset ):
        res = results[0]
    else:
        res = results[1]    
    
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar acción']}, ]
    res = results[0]
    
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    productoActual = model.Acciones.idacciones == idPila
    query = model.db.session.query(model.EstadoActual).filter(productoActual).all()
    
    id_accion = query[0].id_accion_actual
    nueva_descripcion_acciones = params['descripcion']

    accionModif = clsAccion()
    resultsModif = accionModif.modify_Accion(id_accion, nueva_descripcion_acciones)

    if ( resultsModif ):
        res = results[0]
    else:
        res = results[1]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@accion.route('/accion/VAccion')
def VAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    res['idPila'] = 1

    pagAccionActual = request.url
    pagAccionActual.split('=')
    accionActual = int(pagAccionActual[-1])

    productoActual = model.EstadoActual.id_producto_actual == 1
    model.db.session.query(model.EstadoActual).filter(productoActual).\
        update({'id_accion_actual':accionActual})
    model.db.session.commit()

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.