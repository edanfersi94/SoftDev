# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
import model

actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]

    nuevo_nombre_actores      = params['nombre']
    nueva_descripcion_actores = params['descripcion']
    
    # Se obtiene la información del estado de la página.
    query = model.db.session.query(model.EstadoActual).all()
    idProducto = int(query[0].id_producto_actual)

    nuevoActor   = clsActor()
    resultInsert = nuevoActor.insert_Actor( idProducto, nuevo_nombre_actores, nueva_descripcion_actores)

    if ( resultInsert ):
        res = results[0]
    else:
        res = results[1]

    res['label'] = res['label'] + '/' + str(idProducto)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    # Se obtiene la información del estado de la página.
    query = model.db.session.query(model.EstadoActual).all()

    idPila = int(query[0].id_producto_actual)
    res['label'] = res['label'] + '/' + str(idPila)

    id_actor = query[0].id_actor_actual
    nuevo_nombre_actores = params['nombre']
    nueva_descripcion_actores = params['descripcion']

    actorModif = clsActor()
    resultsModif = actorModif.modify_Actor( idPila, id_actor, nuevo_nombre_actores, nueva_descripcion_actores)

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



@actor.route('/actor/VActor')
def VActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    # Se obtiene la información del estado de la página.
    query = model.db.session.query(model.EstadoActual).all()
    idProducto = int(query[0].id_producto_actual)

    res['idPila'] = idProducto

    pagActorActual= request.url
    pagActorActual.split('=')
    actorActual = int(pagActorActual[-1])

    model.db.session.query(model.EstadoActual).update({'id_actor_actual':actorActual})
    model.db.session.commit()    

    return json.dumps(res)

@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Datos de prueba
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here
