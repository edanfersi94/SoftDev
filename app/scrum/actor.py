# -*- coding: utf-8 -*-

# Librerias a importar.
from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
import model

actor = Blueprint('actor', __name__)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]

    nuevo_nombre_actores      = params['nombre']
    nueva_descripcion_actores = params['descripcion']
    
    nuevoActor   = clsActor()
    resultInsert = nuevoActor.insert_Actor(nuevo_nombre_actores, nueva_descripcion_actores)

    if ( resultInsert ):
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

@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    productoActual = model.EstadoActual.id_producto_actual == idPila
    query = model.db.session.query(model.EstadoActual).filter(productoActual).all()
    
    id_actor = query[0].id_actor_actual
    nuevo_nombre_actores = params['nombre']
    nueva_descripcion_actores = params['descripcion']

    actorModif = clsActor()
    resultsModif = actorModif.modify_Actor(id_actor, nuevo_nombre_actores, nueva_descripcion_actores)

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

@actor.route('/actor/VActor')
def VActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    res['idPila'] = 1 

    pagActorActual= request.url
    pagActorActual.split('=')
    actorActual = int(pagActorActual[-1])

    productoActual = model.EstadoActual.id_producto_actual == 1
    model.db.session.query(model.EstadoActual).filter(productoActual).\
        update({'id_actor_actual':actorActual})
    model.db.session.commit()    

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.