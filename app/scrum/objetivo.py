# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcObjetivo import clsObjetivo
import model

objetivo = Blueprint('objetivo', __name__)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[1]
    
    # Descripción del objetivo a crear.
    nueva_descripcion_objetivo = params['descripcion']

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    nuevoObjetivo = clsObjetivo()
    resultInset = nuevoObjetivo.insert_Objetivo( idProducto, nueva_descripcion_objetivo)

    if ( resultInset ):
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

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[1]
    
    # Se obtiene el identificador del producto actual.
    idPila = int(session['idPila'])

    # Se obtiene los atributos del objetivo a modificar.
    id_objetivo = int(session['idObjetivo'])
    nueva_descripcion_objetivo = params['descripcion']

    objetivoModif = clsObjetivo()
    resultsModif  = objetivoModif.modify_Objetivo(idPila, id_objetivo, nueva_descripcion_objetivo)

    if ( resultsModif ):
        res = results[0]
        # Se actualiza el URL de la pág a donde se va a redirigir.
        res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}

    # Producto actual.
    idProducto = session['idPila']

    # Se almacena la información recibida.
    res['fObjetivo'] = {'idPila': idProducto,
                        'idObjetivo':request.args.get('idObjetivo',1),
                        'descripcion':request.args.get('descripcion')}
    res['idPila'] = idProducto

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProducto = int(request.args.get('idPila',1))

    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador del objetivo actual.
    idObjetivoActual = int(request.args.get('idObjetivo',1))
    session['idObjetivo'] = idObjetivoActual

    # Se obtiene la información del objetivo a modificar.
    infoObjActual = model.db.session.query(model.Objetivo).filter_by(idObjetivo = idObjetivoActual)
    descripcionObjetivoActual = infoObjActual[0].descripObjetivo

    # Se almacena la información a enviar.
    res['fObjetivo'] = {'idPila': idProducto,
                        'idObjetivo':idObjetivoActual,
                        'descripcion':descripcionObjetivoActual}


    return json.dumps(res)

#.----------------------------------------------------------------------------------------.