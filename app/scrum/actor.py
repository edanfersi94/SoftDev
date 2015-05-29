# -*- coding: utf-8 -*-

# Librerias a importar.
from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
from app.scrum.mdlaccesscontrol import clsAccessControl
import model

actor = Blueprint('actor', __name__)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[1]

    # Información del actor a crear.
    nuevo_nombre_actores      = params.get('nombre',None)
    nueva_descripcion_actores = params.get('descripcion', None)
   
    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    if(( nuevo_nombre_actores != None ) and ( nueva_descripcion_actores != None )):
        accessControl = clsAccessControl()
        resultCheck = accessControl.check_descripcion( nueva_descripcion_actores )

        if ( resultCheck ):
            nuevoActor   = clsActor()
            resultInsert = nuevoActor.insert_Actor( idProducto, nuevo_nombre_actores, nueva_descripcion_actores)

            if ( resultInsert ):
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

@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idPila = int(session['idPila'])

    # Se obtiene los atributos del actor actual.
    id_actor = int(session['idActor'])
    nuevo_nombre_actores = params['nombre']
    nueva_descripcion_actores = params['descripcion']

    actorModif = clsActor()
    resultsModif = actorModif.modify_Actor( idPila, id_actor, nuevo_nombre_actores, nueva_descripcion_actores)

    if ( resultsModif ):
        res = results[0]

    # Se actualiza el URL de la pág a donde se va a redirigir.
    res['label'] = res['label'] + '/' + str(id_actor)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}

    # Producto actual.
    idProducto = request.args.get('idPila',1)

    # Se almacena la información recibida.
    res['fActor'] = {'idPila':idProducto,
                     'idActor':request.args.get('idActor',1),
                     'descripcion':request.args.get('descripcion')}
    res['idPila'] = idProducto

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/VActor')
def VActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProducto = session['idPila']
    
    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador del actor actual.
    idActorActual = int(request.args.get('idActor',1))
    session['idActor'] = idActorActual

    # Se obtiene la información del actor a modificar.
    infoActorActual = model.db.session.query(model.Actores).filter_by(id_actores = idActorActual)
    nombreActorActual = infoActorActual[0].nombre_actores
    descripcionActorActual = infoActorActual[0].descripcion_actores

    res['fActor'] = {'idPila': idProducto,
                     'nombre':nombreActorActual,
                     'descripcion':descripcionActorActual}

    return json.dumps(res)

#.----------------------------------------------------------------------------------------.