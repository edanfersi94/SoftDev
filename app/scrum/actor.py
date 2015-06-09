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
        eliminar actores.
"""
#.-----------------------------------------------------------------------------.

# Librerias a importar.
from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
from app.scrum.controlDeAcceso import clsControlDeAcceso
from model import db, Actores

actor = Blueprint('actor', __name__)

#.-----------------------------------------------------------------------------.

@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():

    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']},
               {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    # Parámetros del actor a crear.
    nombre = params.get('nombre',None)
    descripcion = params.get('descripcion', None)
   
    if( ( nombre != None ) and ( descripcion != None ) ):
        controlDeAcceso = clsControlDeAcceso()
        descripcionValida = controlDeAcceso.verificarDescripcion( descripcion )

        if ( descripcionValida ):
            nuevoActor = clsActor()
            creacionCorrecta = nuevoActor.insertar(idProducto,nombre,descripcion)

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
@actor.route('/actor/AElimActor')
def AElimActor():
    #GET parameter
    identificador = request.args['idActor']
    results = [{'label':'/VProducto', 'msg':['Actor eliminado']}, {'label':'/VActor', 'msg':['No se pudo eliminar este actor']}, ]
    res = results[1]
    
    actor = clsActor()
    eliminarCorrecto = actor.eliminar(identificador)

    if(eliminarCorrecto):
        res = res[0]

    res['label'] = res['label'] + '/' + + str(identificador)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.------------------------------------------------------------------------------.

@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, 
               {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[1]

    # Se obtiene el identificador del producto actual.
    idProducto = int(session['idPila'])

    # Se obtiene los atributos del actor a modificar.
    identificador = int(session['idActor'])
    nombre = params.get('nombre', None)
    descripcion= params.get('descripcion', None)

    if ((nombre != None) and (descripcion != None)):
        actor = clsActor()
        modificacionCorrecta = actor.modificar(identificador,nombre,descripcion)

        if ( modificacionCorrecta ):
            res = results[0]
            res['label'] = res['label'] + '/' + str(idProducto)

    # Se actualiza el URL de la pág a donde se va a redirigir.
    if (res == results[1]):
        res['label'] = res['label'] + '/' + str(identificador)
    res['idPila'] = idProducto    

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}

    # Producto actual.
    idProducto = session['idPila']

    # Se almacena la información recibida.
    res['fActor'] = {'idPila':idProducto,
                     'idActor':request.args.get('idActor',1),
                     'descripcion':request.args.get('descripcion')}
    res['idPila'] = idProducto

    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)

#.-----------------------------------------------------------------------------.

@actor.route('/actor/VActor')
def VActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    idProducto = int(session['idPila'])
    
    # Se envía el identificador del producto al que pertenece el producto actual.
    res['idPila'] = idProducto

    # Se obtiene el identificador del actor actual.
    identificador = int(request.args.get('idActor',1))
    session['idActor'] = identificador

    # Se obtiene la información del actor a modificar.
    accionBuscada = db.session.query(Actores).\
                        filter(Actores.identificador == identificador).\
                        first()
    nombre = accionBuscada.nombre
    descripcion = accionBuscada.descripcion

    res['fActor'] = {'idPila': idProducto,
                     'nombre':nombre,
                     'descripcion':descripcion}

    return json.dumps(res)

#.-----------------------------------------------------------------------------.