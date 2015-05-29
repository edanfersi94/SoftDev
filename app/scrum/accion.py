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
    res = results[1]

    # Descripción de la acción a crear.
    nueva_descripcion_acciones = params['descripcion']

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    nuevaAccion = clsAccion()
    resultInset = nuevaAccion.insert_Accion( idProducto, nueva_descripcion_acciones)

    if ( resultInset ):
        res = results[0]
        # Se actualiza el URL.
        res['label'] = res['label'] + '/' + str(idProducto)

    res['idPila'] = idProducto

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
    res = results[1]
    
    # Se obtiene el identificador del producto actual.
    idPila = int(session['idPila'])
    
    # Se obtiene los atributos de la acción a modificar.
    id_accion = int(session['idAccion'])
    nueva_descripcion_acciones = params['descripcion']

    accionModif = clsAccion()
    resultsModif = accionModif.modify_Accion( idPila, id_accion, nueva_descripcion_acciones)

    if ( resultsModif ):
        res = results[0]
        # Se actualiza el URL.
        res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}

    # Producto actual.
    idProducto = session['idPila']

    # Se almacena la información recibida.
    res['fAccion'] = {'idPila':idProducto,
                      'idAccion':request.args.get('idAccion',1),
                      'descripción':request.args.get('descripcion')}
    res['idPila'] = idProducto

    if "actor" in session:
        res['actor']=session['actor']

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@accion.route('/accion/VAccion')
def VAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    idProducto = int(request.args.get('idPila',1))

    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador de la acción actual.
    idAccionActual = int(request.args.get('idAccion',1))
    session['idAccion'] = idAccionActual

    # Se obtiene la información del objetivo a modificar.
    infoAccionActual = model.db.session.query(model.Acciones).filter_by(idacciones = idAccionActual)
    descripcionAccionActual = infoAccionActual[0].descripAcciones

    # Se almacena la información a enviar.
    res['fAccion'] = {'idPila': idProducto,
                      'idAccion':idAccionActual,
                      'descripcion':descripcionAccionActual}

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.