# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcObjetivo import clsObjetivo
import model

objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    # Se obtiene la información del estado de la página.
    query = model.db.session.query(model.EstadoActual).all()
    idProducto = int(query[0].id_producto_actual)

    nuevoObjetivo = clsObjetivo()
    resultInset = nuevoObjetivo.insert_Objetivo( idProducto, nueva_descripcion_objetivo)

    if ( resultInset ):
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



@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[0]
    
    # Se obtiene la información del estado de la página.
    query = model.db.session.query(model.EstadoActual).all()

    idPila = int(query[0].id_producto_actual)
    res['label'] = res['label'] + '/' + str(idPila)
    
    id_objetivo = query[0].id_objetivos_actual
    nueva_descripcion_objetivo = params['descripcion']

    objetivoModif = clsObjetivo()
    resultsModif  = objetivoModif.modify_Objetivo(idPila, id_objetivo, nueva_descripcion_objetivo)

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



@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    #Datos de prueba
    res['idPila'] = 1

    #Action code ends here
    return json.dumps(res)



@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
         
    # Se obtiene la información del estado de la página.
    query = model.db.session.query(model.EstadoActual).all()
    idProducto = int(query[0].id_producto_actual)

    res['idPila'] = idProducto

    pagActorActual= request.url
    pagActorActual.split('=')
    objetivoActual = int(pagActorActual[-1])

    model.db.session.query(model.EstadoActual).update({'id_objetivos_actual':objetivoActual})
    model.db.session.commit()   

    return json.dumps(res)





#Use case code starts here


#Use case code ends here
