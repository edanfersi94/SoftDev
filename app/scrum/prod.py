# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.funcActor import clsActor
import model


prod = Blueprint('prod', __name__)


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, ]
    res = results[0]

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    return json.dumps(res)



@prod.route('/prod/VProducto')
def VProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    actores = model.Actores.query.all()
    acciones = model.Acciones.query.all()
    objetivos = model.Objetivo.query.all()

    if (request.args.get('idPila', 1) == 'undefined'):
        idPila = 1
    else:
        idPila = int(request.args.get('idPila', 1))

    productosListados = model.EstadoActual.query.all()
    if ( len(productosListados) == 0):
        producto1 = model.EstadoActual(1)
        model.db.session.add(producto1)
        model.db.session.commit()
    
    pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}]
    res['fPila'] = pilas[idPila-1]
    res['data3'] = [
        {'idActor':act.id_actores, 'nombre':act.nombre_actores,'descripcion':act.descripcion_actores}
        for act in actores]
    res['data5'] = [
        {'idAccion':acc.idacciones, 'descripcion':acc.descripAcciones}
         for acc in acciones]
    res['data7'] = [
        {'idObjetivo':obj.idObjetivo, 'descripcion':obj.descripObjetivo}
         for obj in objetivos]
    res['idPila'] = idPila    
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    res['data0'] = [{'idPila':1, 'nombre':'Pagos en línea'} ]

    actoresListados = model.Actores.query.all()
    if ( len(actoresListados) == 0 ):
        nuevoActor = clsActor()
        nuevoActor.insert_Actor('Product Owner','Es el dueño del producto')
        nuevoActor.insert_Actor('Scrum Master','Es el Maestro Scrum del producto')
        nuevoActor.insert_Actor('Developer','Es el desarrollador del producto')

    return json.dumps(res)