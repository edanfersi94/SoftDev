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
    res = results[0]
    
    nueva_descripcion_objetivo = params['descripcion']

    nuevoObjetivo = clsObjetivo()
    resultInset = nuevoObjetivo.insert_Objetivo( nueva_descripcion_objetivo)

    if ( resultInset ):
        res = results[0]
    else:
        res = results[1]    
       
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila) # falta agregar el id de la pila

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
    res = results[0]
    
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    productoActual = model.EstadoActual.id_producto_actual == idPila
    query = model.db.session.query(model.EstadoActual).filter(productoActual).all()
    
    id_objetivo = query[0].id_objetivos_actual
    nueva_descripcion_objetivo = params['descripcion']

    objetivoModif = clsObjetivo()
    resultsModif  = objetivoModif.modify_Objetivo(id_objetivo, nueva_descripcion_objetivo)

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

@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
  
    res['idPila'] = 1 

    pagActorActual= request.url
    pagActorActual.split('=')
    objetivoActual = int(pagActorActual[-1])

    productoActual = model.EstadoActual.id_producto_actual == 1
    model.db.session.query(model.EstadoActual).filter(productoActual).\
        update({'id_objetivos_actual':objetivoActual})
    model.db.session.commit()   

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.